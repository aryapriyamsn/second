from django.conf.urls import url
from .views import login,register,dashboard,logout



urlpatterns = [
    url(r'^login/$', login, name='vendor_login'),
    url(r'^register/$',register,name='vendor_register'),
    url(r'^vendor-dashboard/$', dashboard, name='vendor_dashboard'),
    url(r'^logout/$',logout,name='vendor_logout'),
    
]