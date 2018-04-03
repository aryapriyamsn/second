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
	import ipdb; ipdb.set_trace()
	user=User.objects.get(username=username)
	user = Users.objects.get(u_name=user)
	customers = Customers.objects.all()
	for item in customers:
		vendor=str(item.vendor)
	context={
		'nbar':'profile',
		'abar':'vendor',
		'vendor': vendor,}

	context.update(csrf(request))
	return render(request,"vendor.html",context)
