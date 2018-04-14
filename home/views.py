from django.shortcuts import render,HttpResponseRedirect
from users.models import Users
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def Home(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		context = {
			"user" : user,
			'nbar' :'home',
		}
		return render(request,"home.html",context)
	else:
		user=request.user
		context = {
			'user' : user,
			'nbar' : 'home',
		}

	return render(request,"home.html",context)


def Home2(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		
		context = {
			"user" : user,
			'nbar' : 'home',
		}
	else:
		user= str(request.user)
		context = {
			'user' : user,
			'nbar' : 'home',
		}
	return render(request,"home.html",context)


def req_contact(request):
	if request.method =="POST":
		mob_no = request.POST.get("contact")
		subject = "contact requested"
		message = "Customer with contact no. "+mob_no+" has requested to connect."
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)
	return HttpResponseRedirect("/")
def digest(request):
	context={
		'nbar':"digest",
	}
	return render(request,'digest.html',context)

def home(request):
	
	return render(request,'home.html',{'nbar' : 'home',})

def contact(request):
	return  render(request,'contact.html',{'nbar' : 'contact',})

def faqs(request):
	
	return render(request,'faqs.html',{'nbar' : 'faqs',})

def account(request):
	
	return render(request,'account.html',{'nbar' : 'account',})

def about(request):
	
	return render(request,'about.html',{'nbar' : 'about',})

def workwithus(request):
	
	return render(request,'workwithus.html',{'nbar' : 'workwithus',})

def privacy(request):
	
	return render(request,'privacypolicy.html',{'nbar' : 'privacy',})

	
def welcome(request):
	return render(request,'welcome.html',{'nbar' : 'privacy',})
def dummy(request):
	return render(request,'dummy.html',{'nbar' : 'privacy',})


