from django.shortcuts import render, render_to_response,HttpResponseRedirect,get_object_or_404
from django.http import Http404
from django.template.context_processors import csrf
from django.conf import settings
from django.core.mail import send_mail
from .models import Users, UserInfo
import re
from news_subscription.views import subscription_details
from django.contrib.auth.decorators import login_required	
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from news_subscription.models import Subscription
from .forms import UserInfoForm,UsersForm
# Create your views here.

def register(request):
	import ipdb; ipdb.set_trace()
	context = {}
	if request.method == 'POST':
		try:
			name = request.POST.get("u_name")
			mob_no = request.POST.get("mobile")
			email = request.POST.get("email")
			password1 = request.POST.get("password1")
			password2 = request.POST.get("password2")
			if password2 == password1:
				if mob_no.isdigit():
					if not Users.objects.filter(mob_no=mob_no).exists():
						if not Users.objects.filter(email_id=email).exists():
							
							user = User.objects.create_user(
								username=name,
								password=password1,
								email=email)

							user_info = Users(
								u_name=user,
								mob_no = mob_no,
								email_id = email,
								)
							user_info.save()
							subject = "Welcome to Sightnext."
							message = "You are now a proud member of Sightnext.!!!"
							from_email = settings.EMAIL_HOST_USER
							to_email = [user_info.email_id]
							send_mail(
								subject,
								message,
								from_email,
								to_email,
								fail_silently=False,
							)
							context = {
							'success':True,
							'message' : 'Welcome to Sightnext',
							'nbar' : 'signin',

							}
							name = name
							password = password1
							user = auth.authenticate(username = name, password = password)
							if request.user.is_authenticated():
								context={
									'status':"one User already logged in",
									'nbar' : 'account',
									'abar':'profile',}
								context.update(csrf(request))
								return render_to_response("login.html", context)
							else:
								if user is not None:
									if user.is_active:
										auth.login(request,user)
							
							context.update(csrf(request))
							return HttpResponseRedirect("/details/subscription/")
							
						else:
							print("not done email")
							context = {
								'success':False,
								'message': 'email already used',
								'nbar' : 'signin',
							}
							context.update(csrf(request))
							return render_to_response('register.html', context)
					else:
						print("not done pass")
						context = {
							'success':False,
							'message': 'Mobile no. already registered or incorrect',
							'nbar' : 'signin',
						}
						context.update(csrf(request))
						return render_to_response('register.html', context)
				else:
					print("not done num")
					context = {
						'success':False,
						'message': 'Mobile no. is incorrect',
						'nbar' : 'signin',
					}
					context.update(csrf(request))
					return render_to_response('register.html', context)
			else:
				print("password does not match")
				context = {
					'success':False,
					'message': 'Passwords did not match, enter again.',
					'nbar' : 'signin',
				}
				context.update(csrf(request))
				return render_to_response('register.html', context)
		except:
			print("not done name")
			context = {
				'success': False,
				'message':'username already taken. please try again.',
				'nbar' : 'signin',
			}
			context.update(csrf(request))
			return render_to_response('register.html',context)
	else:
		context = {'user': request.user.username,'message': "please fill the form",'nbar' : 'signin',}
		context.update(csrf(request))
		return render_to_response('register.html', context)

def login(request):	
		#import ipdb; ipdb.set_trace();
		context = {}
		if request.method == "GET":
			if request.user.is_authenticated():
				context = {
					'user': 'request.user.username',
					'nbar' : 'account',
					'abar':'profile',
					}
				context.update(csrf(request))
				return render_to_response('login.html', context)
			else:
				context={'user':request.user.username}
				context.update(csrf(request))
				return render(request,'login.html', context)
		else:
			name = request.POST.get('u_name')
			password = request.POST.get('password')

			if "@" in name:
				if Users.objects.filter(email_id=name).exists():
					name=Users.objects.get(email_id=name)
					name=str(name.u_name)
				else:
					context={'status':"invalid login details",'user':request.user.username}	
					return render_to_response("register.html", context)
			if re.search('[a-z A-Z]',name)==None:
				if Users.objects.filter(mob_no=name).exists():
					name=Users.objects.get(mob_no=name)
					name=str(name.u_name)
				else:
					context={'status':"invalid login details"}
					context.update(csrf(request))
					return render_to_response("register.html", context)

			user = auth.authenticate(username = name, password = password)
			if not Users.objects.filter(u_name=user).exists():
				context={'status':"invalid login details"}
				context.update(csrf(request))
				return render_to_response("vendor-login.html", context)
			if request.user.is_authenticated():
				context={
					'status':"one User already logged in",
					'nbar' : 'account',
					'abar':'profile',}
				context.update(csrf(request))
				return render_to_response("login.html", context)
			else:
				if user is not None:
					if user.is_active:
						auth.login(request,user)
						user=request.user
						user= Users.objects.get(u_name=user)
						if (UserInfo.objects.filter(user_link=user).exists()):
							user_i= UserInfo.objects.get(user_link=user)
							context = {
							'status' : "login successfull",
							"user" : user_i.full_name,
							'nbar' : 'account',
							'abar':'profile',
							}
						else:
							context = {
								'status' : "login successfull",
								'nbar' : 'account',
								'abar':'profile',
							}
						
						
						context.update(csrf(request))
						return HttpResponseRedirect("/details/subscription/")
					else:
						context = {
							'status' : "Account Deactivated",
							'nbar' : 'account',
							'abar':'profile',
							}	
				else:
					context = {"status" : "invalid login details", "user": request.user.username,'nbar' : 'account','abar':'profile',}
					context.update(csrf(request))
					return render_to_response("login.html",context)


		

@login_required(login_url='/users/login/')
def logout(request):
	#import ipdb; ipdb.set_trace()
	context={}
	if request.user.is_authenticated():
		auth.logout(request)
		context={'status': 'Logout successfull','nbar' : 'account',}
		context.update(csrf(request))
		return login(request)
	else:
		auth.logout(request)
		context={'status' :'Logout successfull','nbar' : 'account',}
		context.update(csrf(request))
		return login(request)

@login_required(login_url='/users/login/')
def loginuser(request,username):
	#import ipdb; ipdb.set_trace()
	instance = User.objects.get(username=username)
	instance= Users.objects.get(u_name=instance)
	if Subscription.objects.filter(sub_user=instance).exists():
		user=request.user.username
	else:
		user=None
	if UserInfo.objects.filter(user_link=instance).exists():
		userinfo=UserInfo.objects.get(user_link=instance)
		if (username==request.user.username):

			if request.method == "GET":

				if request.user.is_authenticated():
					
					context={
					'user': user,
					'nbar' : 'account',
					'abar':'profile',
					"name" : userinfo.full_name,
					"sex" : userinfo.sex,
					"pic" : userinfo.profile_pic,
					"email" :instance.email_id,
					"username" : instance.u_name,
					"contact_no" : instance.mob_no,
					"joining_date" : instance.joining_date,}
					context.update(csrf(request))
					return render(request,'profile.html',context)
				else:
					context={
					'user': user,
					'nbar' : 'account',
					'abar':'profile',
					"name" : userinfo.full_name,
					"sex" : userinfo.sex,
					"pic" : userinfo.profile_pic,
					"email" :instance.email_id,
					"username" : instance.u_name,
					"contact_no" : instance.mob_no,
					"joining_date" : instance.joining_date,}
					
			else:
				context={
					'user': user,
					'nbar' : 'account',
					"name" : userinfo.full_name,
					"sex" : userinfo.sex,
					"pic" : userinfo.profile_pic,
					"email" :instance.email_id,
					'abar':'profile',
					"username" : instance.u_name,
					"contact_no" : instance.mob_no,
					"joining_date" : instance.joining_date,}
				
	else:
		context={
			"user":user,
			"email" :instance.email_id,
			"username" : instance.u_name,
			"contact_no" : instance.mob_no,
			'abar':'profile',
			"joining_date" : instance.joining_date,
			'nbar' : 'account',

		}
	context.update(csrf(request))
	return render(request,'profile.html',context)
		

'''@login_required(login_url='users/(?P<username>[\w.@+-]+)/')
def profile_update(request,username):
	#import ipdb; ipdb.set_trace()
	title = "Update your profile here."
	instance=get_object_or_404(User,username=username)
	if request.method =="GET":
		form = UserInfoForm(request.POST or None)
		context = {
			"title": title,
			"form": form
		}	
	else:
		user = request.user
		user = Users.objects.get(u_name=user)
		form = UserInfoForm(request.POST,request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user_link=user
			instance.save()

		print request.POST.get('full_name')
		print request.POST.get('sex')
		context = {
			"title": "thanks for telling us more about you.",
		}

			
	context.update(csrf(request))
	return render(request, "profile entry.html",context)
	'''

@login_required(login_url='users/(?P<username>[\w.@+-]+)/')
def profile_edit(request,username):
	#import ipdb; ipdb.set_trace()
	title = "Edit Our Profile Here"

	instance=get_object_or_404(User,username=username)
	instance = Users.objects.get(u_name=instance)
	if Subscription.objects.filter(sub_user=instance).exists():
		user1=request.user.username
	else:
		user1=None
	if UserInfo.objects.filter(user_link=instance).exists():
		instance = UserInfo.objects.get(user_link=instance)
		if request.method =="GET":
			form = UserInfoForm(request.POST or None,instance=instance)
			context = {
				"title": title,
				"form": form,
				'nbar' : 'account',
				'abar':'profile',
				'user':user1,
				'pic':instance.profile_pic,
			}
			context.update(csrf(request))
			return render(request, "profile entry.html",context)	
		else:

			user = request.user
			user = Users.objects.get(u_name=user)
			form = UserInfoForm(request.POST,request.FILES or None, instance=instance)
			if form.is_valid():
				instance = form.save(commit=False)
				
				instance.save()

			print request.POST.get('full_name')
			print request.POST.get('sex')
			context = {
				"title": "thanks for telling us more about you.",
				'nbar' : 'account',
				'abar':'profile',
				'user':user1,
			}
			context.update(csrf(request))
			return subscription_details(request)
	else:
		if request.method =="GET":
			form = UserInfoForm(request.POST or None)
			context = {
				"title": title,
				"form": form,
				'nbar' : 'account',
				'abar':'profile',
				'user':user1,
			}	
			context.update(csrf(request))
			return subscription_details(request)
		else:
			user = request.user
			user = Users.objects.get(u_name=user)
			form = UserInfoForm(request.POST,request.FILES or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user_link=user
				instance.save()

			print request.POST.get('full_name')
			print request.POST.get('sex')
			context = {
				"title": "thanks for telling us more about you.",
				'nbar' : 'account',
				'abar':'profile',
				'user':user1,	
			}
			context.update(csrf(request))
			return subscription_details(request)
				
	context.update(csrf(request))
	return render(request, "profile.html",context)


def profile(request,username):
	#import ipdb; ipdb.set_trace()
	instance = User.objects.get(username=username)
	instance= Users.objects.get(u_name=instance)
	if Subscription.objects.filter(sub_user=instance).exists():
		user=request.user.username
	else:
		user=None
	if UserInfo.objects.filter(user_link=instance).exists():
		userinfo=UserInfo.objects.get(user_link=instance)
		context={
		"user":user,
		"name" : userinfo.full_name,
		"sex" : userinfo.sex,
		"pic" : userinfo.profile_pic,
		"email" :instance.email_id,
		"username" : instance.u_name,
		"contact_no" : instance.mob_no,
		"address" : userinfo.address,
		'area_code':userinfo.area_code,
		'abar':'profile',
		"joining_date" : instance.joining_date,
		'nbar' : 'account',

		}
	else:
		context={
			"user":user,
			"email" :instance.email_id,
			"username" : instance.u_name,
			"contact_no" : instance.mob_no,
			"address" : instance.address,
			'abar':'profile',
			"joining_date" : instance.joining_date,
			'nbar' : 'account',

		}
	context.update(csrf(request))
	return render(request, "profile.html", context)