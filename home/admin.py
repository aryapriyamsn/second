from django.contrib import admin
from .views import Home

# Register your models here.
admin.site.urls(Home)
