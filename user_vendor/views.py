from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .models import Customers
from users.models import Users
from Vendor.models import Vendor  


# Create your views here.
@login_required(login_url='/users/login/')
def user_vendor(request,username):
	#import ipdb; ipdb.set_trace()
	context={}
	user=User.objects.get(username=username)
	user = Users.objects.get(u_name=user)
	customers = Customers.objects.all()
	if Customers.objects.filter(customer=user).exists():
		user=Customers.objects.get(customer=user)
		all_vendors=[]
		vendor_list= user.vendor.all()
		for item in vendor_list:
			all_vendors.append(item)
		context={
			'nbar':'profile',
			'abar':'vendor',
			'vendor': all_vendors,}
	else:
		context={'abar':'vendor',}
	context.update(csrf(request))
	return render(request,"vendor.html",context)
