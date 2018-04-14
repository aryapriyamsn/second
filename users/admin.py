from django.contrib import admin
from .models import Users, UserInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ['id','u_name','mob_no','joining_date','email_id']


class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['full_name','sex']


admin.site.register(Users,UserAdmin)
admin.site.register(UserInfo,UserInfoAdmin)