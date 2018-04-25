from django import forms
from .models import UserInfo,Users

class UserInfoForm(forms.ModelForm):
	mob_no=forms.IntegerField()
	class Meta :
		model = UserInfo
		fields = [
			'full_name',
			'address',
			'mob_no',
			'area_code',
			'sex',
			'profile_pic'
		]

class UsersForm(forms.ModelForm):
	class Meta :
		model = Users
		fields = [
			'u_name',
			'mob_no',
			'email_id',
		]