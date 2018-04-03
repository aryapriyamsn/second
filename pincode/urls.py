from django.conf.urls import url
from .views import check

urlpatterns=[
	url(r'^check/$',check,name="check"),
]