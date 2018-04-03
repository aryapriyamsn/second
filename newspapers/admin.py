from django.contrib import admin
from .models import Newspapers

# Register your models here.
class NewspaperAdmin(admin.ModelAdmin):
	
	list_display = ('id','title','languages','price')

	def languages(self, obj):
		return "".join([l for l in obj.language])


admin.site.register(Newspapers, NewspaperAdmin)