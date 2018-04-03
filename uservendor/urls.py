from django.conf.urls import url 
from .views import user_vendor

urlpatterns=[
	url(r'^myvendor/(?P<username>[\w.@+-]+)/$',user_vendor,name="myvendor")
]