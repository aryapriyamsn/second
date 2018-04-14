from django.shortcuts import render
from django.shortcuts import render, render_to_response,HttpResponseRedirect,get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Vendor
from newspapers.models import Newspapers 
import datetime
from news_subscription.models import SubscribePaper
import re
# Create your views here.

def login(request):
	import ipdb; ipdb.set_trace()
	context={}
	if request.method == "GET":
		if request.user.is_authenticated():
			context = {
				'user': 'request.user.username',
				'nbar' : 'dashboard',
				'abar':'profile',
				}
			context.update(csrf(request))
			return render_to_response('vendor-login.html', context)
		else:
			context={'user':request.user.username}
			context.update(csrf(request))
			return render(request,'vendor-login.html', context)
	else:
		name = request.POST.get('u_name')
		password = request.POST.get('password')

		if "@" in name:
			if Vendor.objects.filter(email_id=name).exists():
				name=Vendor.objects.get(email_id=name)
				name=str(name.username)
			else:
				context={'status':"invalid login details"}
				context.update(csrf(request))
				return render_to_response("vendor-login.html", context)
		if re.search('[a-z A-Z]',name)==None:
			if Vendor.objects.filter(mob_no=name).exists():
				name=Vendor.objects.get(mob_no=name)
				name=str(name.username)
			else:
				context={'status':"invalid login details"}
				context.update(csrf(request))
				return render_to_response("vendor-login.html", context)
		
		user = auth.authenticate(username = name, password = password)
		if not Vendor.objects.filter(username=user).exists():
			context={'status':"invalid login details"}
			context.update(csrf(request))
			return render_to_response("vendor-login.html", context)

		if request.user.is_authenticated():
			context={
			'status':"one User already logged in",
				'nbar' : 'account',
				'user':user,
				'abar':'profile',}
			context.update(csrf(request))
			return render_to_response("vendor-login.html", context)
		else:
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					user=request.user
					user= Vendor.objects.get(username=user)
					context = {
					'status' : "login successfull",
					"user" : user,
					'nbar' : 'dashboard',
					'abar':'profile',
					}	
					context.update(csrf(request))
					return HttpResponseRedirect("/vendor-admin/vendor-dashboard/")
				else:
					context = {
						'status' : "Account Deactivated",
						'nbar' : 'account',
						'abar':'profile',
						}	
			else:
				context = {"status" : "invalid login details", "user": request.user.username,'nbar' : 'account','abar':'profile',}
				context.update(csrf(request))
				return render_to_response("vendor-login.html",context)



def register(request):
	context={}
	return render(request,'vendor-login.html',context)
@login_required(login_url="/vendor-admin/login/")
def logout(request):
	context={}
	if request.user.is_authenticated():
		auth.logout(request)
		context={'status': 'Logout successfull','nbar' : 'account',}
		context.update(csrf(request))
		return render_to_response("vendor-login.html",context)
	else:
		auth.logout(request)
		context={'status' :'Logout successfull','nbar' : 'account',}
		context.update(csrf(request))
		return render_to_response("vendor-login.html",context)

@login_required(login_url="/vendor-admin/login/")
def dashboard(request):
	import ipdb; ipdb.set_trace()
	user=request.user
	user=User.objects.get(username=user)
	vendor=Vendor.objects.get(username=user)
	today=datetime.date.today()
	total=0
	if SubscribePaper.objects.filter(vendor=vendor).exists():
		vendor_papers=[]
		vendor_list=SubscribePaper.objects.all()
		for item in vendor_list:
			start=item.start_date
			if today>=start:
				if datetime.datetime.now().time().hour>8:
					days=(today-start).days
				else:
					days=(today-start).days-1
				bill=0
				paper=str(item.sub_paper)
				paper=Newspapers.objects.get(title=paper)
				amount=paper.price
				bill+=days*amount
				SubscribePaper.objects.filter(sub_paper=paper).update(bill=bill,days=days)
			else:
				bill=0
				days=0
			if item.vendor==vendor:
				vendor_papers.append(item)
				total+=item.bill
				start=item.start_date
				
			
			bill=0
		context={
			'vendor':vendor,
			'vendor_papers':vendor_papers,
			'total':total
		}
	else:
		context={
			'vendor':vendor,
		}
	return render(request,'vendor-dashboard.html',context)



















