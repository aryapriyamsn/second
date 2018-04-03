from django.conf.urls import url
from .views import Subscribe, subscription, editsubscription,Bill,paperbill,allpapers,allbills

urlpatterns = [
	url(r'^new/$', Subscribe, name='subscribe'),
	url(r'^mysubscription/$', subscription, name='subscription'),
	url(r'^edit/$', editsubscription, name='editsubscription'),
	url(r'^bill/$', Bill, name='bill'),
	url(r'^bill/(?P<paper>[\w -()]+)/$', paperbill, name='paperbill'),
	url(r'^account/$', allpapers, name='account'),
	url(r'^allbills/$', allbills, name='allbills'),

]
