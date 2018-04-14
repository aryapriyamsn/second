from django import forms
from .models import Subscription,SubscribePaper
from django.forms import ModelChoiceField
from Vendor.models import Vendor
from functools import partial

DateInput = partial(forms.DateInput,{'class':'datepicker'})



class SubscriptionForm(forms.ModelForm):
	start_date= forms.DateField(widget=DateInput())
	class Meta:
		model = Subscription
		fields = ['sub_paper','start_date','address','pin_code']




class SubscribeForm(forms.ModelForm):
	start_date= forms.DateField(widget=DateInput())
	temp_vendor=forms.CharField(max_length=22)
	class Meta:
		model=SubscribePaper
		fields=['sub_paper','start_date','address','pin_code',"temp_vendor"]

