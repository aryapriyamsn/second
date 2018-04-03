from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .forms import SubscriptionForm
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from users.models import Users,UserInfo
from users.forms import UserInfoForm
from .models import Subscription
from newspapers.models	 import Newspapers 
# Create your views here.

@login_required(login_url='/users/login/')
def Subscribe(request):
	#import ipdb; ipdb.set_trace()
	# papers = Newspapers.objects.all()
	# papers_list=[]
	# queryset=Subscription.objects.all()
	user = request.user
	user = Users.objects.get(u_name=user)
	# for item in papers:
	# 	papers_list.append(str(item.title))
	if request.method == "POST":
		form = SubscriptionForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.sub_user = user
			instance.start_date = str(datetime.date.today())
			instance.save()
			form.save_m2m()
			# if queryset.filter(sub_user=user).exists():
			# 	instance=Subscription.objects.get(sub_user=user)
			# else:
			# 	instance=None	
			if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)
				context = {
					'title' : "thhanksss",
					# 'user':instance,
					'pic':userinfo.profile_pic,
					"name":userinfo.full_name,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'subscription',
				}
			else:
				context = {
						'title' : "thhanksss",
						'nbar' : 'account',
						# 'user':instance,
						# 'papers':papers_list,
						'abar':'subscription',
					}
			return HttpResponseRedirect('/details/mysubscription')
		else:
			# if queryset.filter(sub_user=userr).exists():
			# 	instance=Subscription.objects.get(sub_user=user)
			# else:
				# instance=None
			if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)
				context = {
					'title' : "thhanksss",
					'user':instance,
					'pic':userinfo.profile_pic,
					'title': "sorry",'abar':'subscription',}
			else:
				context={'title': "sorry",'abar':'subscription',}
	else:
		form = SubscriptionForm(request.POST or None)
		# if queryset.filter(sub_user=user).exists():
		# 	instance=Subscription.objects.get(sub_user=user)
		# else:
		# 	instance=None
		if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)
				context = {
					'title' : "thanksss",
					'pic':userinfo.profile_pic,
					# 'user':instance,
					'title':"please fill the form.",
					'form':form,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'subscription',
					}
		else:
			context = {'title':"please fill the form.",'form':form,'nbar' : 'account',	'abar':'subscription',}
		context.update(csrf(request))
	return render(request,'subscribe.html',context)

@login_required(login_url='/users/login/')
def subscription(request):
	#import ipdb; ipdb.set_trace()
	user=request.user
	bill=0
	userr=User.objects.get(username=user)
	userr = Users.objects.get(u_name=userr)
	today=datetime.date.today()
	form_editsubscription = SubscriptionForm(request.POST or None) 
	queryset=Subscription.objects.all()
	if queryset.filter(sub_user=userr).exists():
		user=Subscription.objects.get(sub_user=userr)
		form_editsubscription = SubscriptionForm(request.POST or None, instance=user) 
		user_instance = UserInfo.objects.get(user_link=userr)
		form_editinfo = UserInfoForm(request.POST or None, instance=user_instance)
		papers=user.sub_paper.all()
		start=user.start_date
		if datetime.datetime.now().time().hour>8:
			days=(today-start).days
		else:
			days=(today-start).days-1

		if (len(user.sub_paper.all())>=1):
			for item in papers:
				paper=str(item)
				paper=Newspapers.objects.get(title=paper)
				amount=paper.price
				bill+=days*amount

		if UserInfo.objects.filter(user_link=userr).exists():
			userinfo=UserInfo.objects.get(user_link=userr)
			context={
				'pic':userinfo.profile_pic,
				"name":userinfo.full_name,
				"papers": papers,
				"user":user,
				'days':days,
				'bill':bill,
				'form':form_editsubscription,
				'form_editinfo':form_editinfo,
				"start_date" : user.start_date,
				"message":"You have subscribed for",
				"address":user.address,
				'nbar' : 'account',
				'abar': 'subscription',
			}
		else:
			context={
					"papers": papers,
					"user":user,
					"days":days,
					'bill':bill,
					'form':form_editsubscription,
					"start_date" : user.start_date,
					"message":"You have subscribed for",
					"address":user.address,
					'nbar' : 'account',	
					'abar':'subscription',
				}
	else:
		if queryset.filter(sub_user=userr).exists():
			instance=Subscription.objects.get(sub_user=user)
		else:
			instance=None
		if UserInfo.objects.filter(user_link=userr).exists():
			userinfo=UserInfo.objects.get(user_link=userr)
			context={
				'pic':userinfo.profile_pic,
				"name":userinfo.full_name,
				'user':instance,
				'message':"You have not subscribed for any newspaper till now. start your subscription today!!",
				'nbar' : 'account',
				'abar':'subscription',
				'form':form_editsubscription,
				}
		else:
			context={
				'user':instance,
				'message':"You have not subscribed for any newspaper till now. start your subscription today!!",
				'nbar' : 'account',
				'abar':'subscription',
				'form':form_editsubscription,
			}
	return render(request,"subscription.html",context)

@login_required(login_url='/users/login/')
def editsubscription(request):
	import ipdb; ipdb.set_trace()
	# papers = Newspapers.objects.all()
	# papers_list = []
	# for item in papers:
	# 	papers_list.append(str(item.title))
	form = SubscriptionForm(request.POST or None) 
	user = request.user
	user = get_object_or_404(Users,u_name=user)
	queryset=Subscription.objects.all()
	if queryset.filter(sub_user=user).exists():
		instance=Subscription.objects.get(sub_user=user)
		if request.method == "GET":
			form = SubscriptionForm(request.POST or None, instance=instance)
			if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)
				context={
					'pic':userinfo.profile_pic,
					"name":userinfo.full_name,
					"form" : form,
					'user':instance,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'editsubscription',
				}
			else:
				context={
					"form" : form,
					'user':instance,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'editsubscription',
				}
		else:
			form = SubscriptionForm(request.POST or None, instance=instance)
			if form.is_valid():
				instances= form.save(commit=False)

				instances.save()
				form.save_m2m()
			if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)

				context={
					'pic':userinfo.profile_pic,
					"name":userinfo.full_name,
					"form":form,
					'user':instance,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'editsubscription',
				}
			else:
				context={
					"form":form,
					'user':instance,
					'nbar' : 'account',
					# 'papers':papers_list,
					'abar':'editsubscription',
				}
			return HttpResponseRedirect('/details/mysubscription')
	else:
		if queryset.filter(sub_user=user).exists():
			instance=Subscription.objects.get(sub_user=user)
		else:
			instance=None
		if UserInfo.objects.filter(user_link=user).exists():
			userinfo=UserInfo.objects.get(user_link=user)
			context={
				'pic':userinfo.profile_pic,
				"name":userinfo.full_name,
				'user':instance,
				'form':form,
				'message' : "you have not subscribed for any newspaper till now. ",
				# 'papers':papers_list,
				'abar':'editsubscription',
				}
		else:
			context={'message' : "you have not subscribed for any newspaper till now. ",'form':form,'abar':'editsubscription',}
	context.update(csrf(request))
	return render(request,"subscribe.html",context)

@login_required(login_url='/users/login/')
def Bill(request):
	#import ipdb; ipdb.set_trace()
	bill=0
	user=request.user
	userr=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=userr)
	today=datetime.date.today()
	start=user.start_date
	if datetime.datetime.now().time().hour>8:
		days=(today-start).days
	else:
		days=(today-start).days-1
	
	if (len(user.sub_paper.all())>1):
		queryset = user.sub_paper.all()
		for papers in queryset:
			paper=str(papers)
			paper=Newspapers.objects.get(title=paper)
			amount=paper.price
			bill+=days*amount
	else:
		queryset = user.sub_paper.all()
		paper=str(queryset[0])
		paper=Newspapers.objects.get(title=paper)
		amount=paper.price
		bill+=days*amount
	if UserInfo.objects.filter(user_link=userr).exists():
		userinfo=UserInfo.objects.get(user_link=userr)
		context={
			'pic':userinfo.profile_pic,
			"name":userinfo.full_name,
			"bill":bill,
			'user':user,
			'nbar' : 'account',
			'abar':'bill',
			'days':days,
		}
	else:
		context={
			"bill":bill,
			'nbar' : 'account',
			'user':user,
			'abar':'bill',
		}
	context.update(csrf(request))
	return render(request,"bill.html",context)



@login_required(login_url="/users/login/")
def allpapers(request):
	#import ipdb; ipdb.set_trace()
	user = request.user
	userr=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=userr)

	queryset=user.sub_paper.all()
	querylist=[]
	for paper in queryset:
		querylist.append(str(paper))

	length=len(queryset)
	add = user.address
	mob_no= userr.mob_no
	duration = userr.joining_date
	if UserInfo.objects.filter(user_link=userr).exists():
		userinfo=UserInfo.objects.get(user_link=userr)
		context={
			'pic':userinfo.profile_pic,
			"name":userinfo.full_name,
			"queryset": queryset,
			"length":length,
			'user':user,
			"querylist":querylist,
			"address":add,
			"duration":duration,
			"mob_no":mob_no,
			'nbar' : 'account',
			'abar':'subscription',

		}
	else:
		context={
			"queryset": queryset,
			"length":length,
			"querylist":querylist,
			"address":add,
			'user':user,
			"duration":duration,
			"mob_no":mob_no,
			'nbar' : 'account',
			'abar':'subscription',

		}
	context.update(csrf(request))
	return render(request,"allpaper.html",context)

@login_required(login_url="/user/login")
def paperbill(request,paper):
	#import ipdb; ipdb.set_trace()
	paper=Newspapers.objects.get(title=paper)
	user=request.user
	userr=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=userr)
	today=datetime.date.today()
	start=user.start_date
	if datetime.datetime.now().time().hour>8:
		days=(today-start).days
	else:
		days=(today-start).days-1
	
	bill=days*paper.price
	if UserInfo.objects.filter(user_link=userr).exists():
		userinfo=UserInfo.objects.get(user_link=userr)
		context={
			'pic':userinfo.profile_pic,
			"name":userinfo.full_name,
			"bill": bill,
			'paper':paper,
			'nbar' : 'account',
			'abar':'bill',
			'user':user,
			}
	else:
		context={
			"bill": bill,
			'user':user,
			'paper':paper,
			'nbar' : 'account',
			'abar':'bill',
		}
	return render(request,"paperbill.html",context)

@login_required(login_url="/user/login")
def allbills(request):
	#import ipdb; ipdb.set_trace()
	bill=0
	user=request.user
	userr=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=userr)
	today=datetime.date.today()
	start=user.start_date
	if datetime.datetime.now().time().hour>8:
		days=(today-start).days
	else:
		days=(today-start).days-1
	
	querylist=[]
	queryset = user.sub_paper.all()
	if (len(user.sub_paper.all())>1):
		queryset = user.sub_paper.all()
		for papers in queryset:
			paper=str(papers)
			paper=Newspapers.objects.get(title=paper)
			amount=paper.price
			bill+=days*amount
			querylist.append(str(paper))
	else:
		queryset = user.sub_paper.all()
		paper=str(queryset[0])
		paper=Newspapers.objects.get(title=paper)
		amount=paper.price
		bill+=days*amount
		querylist.append(str(queryset[0]))
	if UserInfo.objects.filter(user_link=userr).exists():
		userinfo=UserInfo.objects.get(user_link=userr)
		context={
			'pic':userinfo.profile_pic,
			"name":userinfo.full_name,
			"bill":bill,
			"querylist":querylist,
			"days": days,
			'user':user,
			"queryset": queryset,
			'nbar' : 'account', 
			'abar' : 'bill',
			}
	else:
		context={
			"bill":bill,
			"querylist":querylist,
			"days": days,
			'user':user,
			"queryset": queryset,
			'nbar' : 'account', 
			'abar' : 'bill',
		}

	context.update(csrf(request))
	return render(request,"allbills.html",context)
