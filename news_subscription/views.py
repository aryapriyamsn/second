from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .forms import SubscriptionForm,SubscribeForm
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from users.models import Users,UserInfo
from users.forms import UserInfoForm
from .models import Subscription,SubscribePaper
from Vendor.models import Vendor
from unpaid.models import Unpaid
from newspapers.models import Newspapers 
# Create your views here.

@login_required(login_url='/users/login/')
def Subscribe_paper(request):
	import ipdb; ipdb.set_trace()
	user=request.user
	user=Users.objects.get(u_name=user)
	today=datetime.date.today()
	if request.method=='POST':
		form = SubscribeForm(request.POST or None)
		if form.is_valid():
			try:
				instance=form.save(commit=False)
				instance.sub_user=user
				temp=request.POST.get("temp_vendor")
				if Vendor.objects.filter(VIN=temp).exists():
					instance.vendor=Vendor.objects.get(VIN=temp_vendor)
				if instance.start_date < today:
					exit()
				instance.save()
			except:
				print("not done pass except")
				context = {
				'message':'please check the filled details, start date should also not be a previous date.',
				'nbar' : 'signin',
				}
				return HttpResponseRedirect('/details/subscription')
				
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
			return HttpResponseRedirect('/details/subscription')
		else:
			# if queryset.filter(sub_user=userr).exists():
			# 	instance=Subscription.objects.get(sub_user=user)
			# else:
				# instance=None
			if UserInfo.objects.filter(user_link=user).exists():
				userinfo=UserInfo.objects.get(user_link=user)
				context = {
					'user':instance,
					'pic':userinfo.profile_pic,
					'title': "sorry",'abar':'subscription',}
			else:
				context={'title': "sorry",'abar':'subscription',}
	else:
		form = SubscribeForm(request.POST or None)
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
	return render(request,'subscrition.html',context)


@login_required(login_url='users/login/')
def subscription_details(request):
	#import ipdb; ipdb.set_trace()
	user=request.user
	user_link=Users.objects.get(u_name=user)
	bill=0
	total=0
	vendors=[]
	today=datetime.date.today()
	edit_form=SubscribeForm(request.POST or None)
	if Unpaid.objects.filter(sub_user=user_link).exists():
		unpaid=Unpaid.objects.filter(sub_user=user_link).all()
	else:
		unpaid=None
	queryset=SubscribePaper.objects.all()
	users_papers=[]
	if queryset.filter(sub_user=user_link).exists():
		# user=SubscribePaper.objects.get(sub_user=user_link)
		# edit_form=SubscribeForm(request.POST or None, instance=user)
		if UserInfo.objects.filter(user_link=user_link).exists():
			logged_user=UserInfo.objects.get(user_link=user_link)
			editinfo_form=UserInfoForm(request.POST or None, instance=logged_user)
		else:
			editinfo_form=UserInfoForm(request.POST or None)

		for item in queryset:
			if item.vendor not in vendors:
				vendors.append(item.vendor)
			if item.sub_user==user_link:
				users_papers.append(item)
				print(item.id)
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
			total+=bill
			bill=0

		Users.objects.filter(u_name=user).update(total_bill=total)	
		if UserInfo.objects.filter(user_link=user_link).exists():
			userinfo=UserInfo.objects.get(user_link=user_link)
			context={
				'pic':userinfo.profile_pic,
				"name":userinfo.full_name,
				'papers':users_papers,
				'vendors':vendors,
				"user":user_link,
				'days':days,
				'unpaid':unpaid,
				'bill':total,
				'form':edit_form,
				'form_editinfo':editinfo_form,
				
				"message":"You have subscribed for",
				
				'nbar' : 'account',
				'abar': 'subscription',
			}
		else:

			context={
					'papers':users_papers,
					"user":user_link,
					"days":days,
					'bill':bill,
					'unpaid':unpaid,
					'vendors':vendors,
					'form':edit_form,
					"message":"You have subscribed for",
					'form_editinfo':editinfo_form,
					'nbar' : 'account',	
					'abar':'subscription',
				}
	else:
		users_papers=None
		if UserInfo.objects.filter(user_link=user_link).exists():
			userinfo=UserInfo.objects.get(user_link=user_link)
			form_editinfo=UserInfoForm(request.POST or None, instance=userinfo)
			context={
				'pic':userinfo.profile_pic,
				"name":userinfo.full_name,
				'user':user_link,
				'papers':users_papers,
				'unpaid':unpaid,
				'message':"You have not subscribed for any newspaper till now. start your subscription today!!",
				'nbar' : 'account',
				'abar':'subscription',
				'vendors':vendors,
				'form':edit_form,
				'form_editinfo':form_editinfo,
				}
		else:
			form_editinfo=UserInfoForm(request.POST or None)

			context={
				'user':user_link,
				'papers':users_papers,
				'message':"You have not subscribed for any newspaper till now. start your subscription today!!",
				'nbar' : 'account',
				'abar':'subscription',
				'vendors':vendors,
				'unpaid':unpaid,
				'form':edit_form,
				'form_editinfo':form_editinfo,
			}
	return render(request,"subscription.html",context)

@login_required(login_url='/users/login/')
def unsubscribe(request,id):
	#import ipdb; ipdb.set_trace()
	user=request.user
	user=Users.objects.get(u_name=user)

	paper=SubscribePaper.objects.get(id=id)
	if (paper.sub_user == user):
		if paper.bill<=0:
			paper.delete()
		else:
			instance=Unpaid(
				sub_user=paper.sub_user,
				sub_paper=paper.sub_paper,
				bill=paper.bill,
				start_date=paper.start_date,
				end_date=datetime.date.today()
				)	
			instance.save()
			paper.delete()

	else: 
		print("make 404 page")
	return subscription_details(request)





# -------------------------------------------------  Old View  -------------------------------------------

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
			form_editinfo=UserInfoForm(request.POST or None, instance=userinfo)
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
	context.update(csrf(request))
	return render(request,"subscription.html",context)


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









