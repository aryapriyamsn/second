from django.shortcuts import render, render_to_response,HttpResponseRedirect
from django.template.context_processors import csrf
from .models import Contact,Newsletter,Work
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def newsletter_entry(request):
	#import ipdb; ipdb.set_trace()
	context={}
	if request.method == "POST":
		recipent_email= request.POST.get("recipent")
		recipent=Newsletter(email=recipent_email)
		recipent.save()
		subject = "Welcome to facelook."
		message = "Thanks for subscribing to our newsletter"
		from_email = settings.EMAIL_HOST_USER
		to_email = [recipent_email]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)
		subject = "New Subscription."
		message = recipent_email+" has joined newsletter reciever"
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)
	context.update(csrf(request))
	return HttpResponseRedirect("/")

def contact_entry(request):
	#import ipdb; ipdb.set_trace()
	context={}
	if request.method == "POST":
		name= request.POST.get("name")
		email=request.POST.get("email")
		message = request.POST.get("message")
		instance=Contact(
			recipent=name,
			email=email,
			message=message,)
		instance.save()
		subject = "user contacted"
		message =  (name + " has requested contact on email-id : "+email+" regarding "+message)
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)
		subject = "no-reply"
		message =  "Thank you for contacting us. We will get back to you as soon as possible."
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)

	context.update(csrf(request))
	return render(request,'contact.html',context)

def work_entry(request):
	import ipdb; ipdb.set_trace()
	context={}
	if request.method == "POST":
		name= request.POST.get("name")
		email=request.POST.get("email")
		message = request.POST.get("message")
		instance=Work(
			requester=name,
			email=email,
			message=message,)
		instance.save()
		subject = "user work query"
		message =  (name + " has requested contact on email-id : "+email+" regarding "+message)
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)
		subject = "no-reply"
		message =  "Thank you for contacting us. We will get back to you as soon as possible."
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(
			subject,
			message,
			from_email,
			to_email,
			fail_silently=False,
		)

	context.update(csrf(request))
	return render(request,'contact.html',context)