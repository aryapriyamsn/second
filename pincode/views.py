from django.shortcuts import render
import re
from django.template.context_processors import csrf
from .models import Pincode,Available
# Create your views here.

def check(request):
	#import ipdb; ipdb.set_trace()
	if request.method=="POST":
		user=str(request.user)
		pin = request.POST.get('pin')
		try:
			if Available.objects.filter(pincode=pin).exists():
				context={
					'user':request.user.username,
					'message':'We got you.',
					'pin':pin,
				}
			elif Pincode.objects.filter(pin=pin).exists():
				context={'user':request.user.username,
					'message':"Sorry! we are currently not in your area. but we will reach you soon. plz subscribe to our email for further updates",
				}
			else:
				context={'user':request.user.username,
					'message':'Sorry! You seem to have entered a wrong pincode'
				}
		except:
			context={'user':request.user.username,
					'message':'Sorry! You seem to have entered a wrong pincode'
				}
	else:
		user=str(request.user)
		context={'user':request.user.username,
			'message': "Check your pincode here"
		}
		return render(request,'pincode-availibility.html',context)
	context.update(csrf(request))
	return render(request,"pincode-response.html",context)