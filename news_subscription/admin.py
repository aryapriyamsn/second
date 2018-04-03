from django.contrib import admin
from .models import Subscription
# Register your models here.

class NewspapersAdmin(admin.ModelAdmin):
	list_display = ['sub_user','sub_papers']

	def sub_papers(self, obj):
		return ", ".join([l.title for l in obj.sub_paper.all()])

admin.site.register(Subscription,NewspapersAdmin)