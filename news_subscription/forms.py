from django import forms
from .models import Subscription
from django.forms import ModelChoiceField
from functools import partial

DateInput = partial(forms.DateInput,{'class':'datepicker'})
class SubscriptionForm(forms.ModelForm):
	start_date= forms.DateField(widget=DateInput())
	class Meta:
		model = Subscription
		fields = ['sub_paper','start_date','address','pin_code']