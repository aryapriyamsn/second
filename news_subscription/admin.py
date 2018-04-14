from django.contrib import admin
from .models import Subscription,SubscribePaper
# Register your models here.

class NewspapersAdmin(admin.ModelAdmin):
	list_display = ['sub_user','sub_papers']

	def sub_papers(self, obj):
		return ", ".join([l.title for l in obj.sub_paper.all()])

admin.site.register(Subscription,NewspapersAdmin)

class SubscribeAdmin(admin.ModelAdmin):
	list_display = ['sub_paper','sub_user',]


admin.site.register(SubscribePaper,SubscribeAdmin)