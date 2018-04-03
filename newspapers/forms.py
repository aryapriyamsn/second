from django import forms

from .models import Newspapers

class NewspaperForms(forms.ModelForm):
	class Meta:
		model = Newspapers
		fields = ['title','language','price','days','area','timing']