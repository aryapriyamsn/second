from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import HttpResponseRedirect
from django.conf import settings
from django.template.context_processors import csrf
from users.models import Users
from django.contrib import auth
class AccountAdapter(DefaultAccountAdapter):

	def get_login_redirect_url(self, request):

		import ipdb; ipdb.set_trace()
		
		user=request.user
		if not Users.objects.filter(email_id=user.email).exists():
			user_info = Users(
				u_name=user,
				email_id = user.email,
				mob_no='9999999999',
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
		
		if user.is_active:
			auth.login(request,user)
			context={'user':request.user.username}
							
		
		return "/details/subscription/"
		