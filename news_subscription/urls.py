from django.conf.urls import url
from .views import Subscribe, subscription, editsubscription,Bill,paperbill,allpapers,allbills,Subscribe_paper,subscription_details,unsubscribe

urlpatterns = [
	url(r'^new/$', Subscribe, name='subscribe'),
	url(r'^new-subscription/$', Subscribe_paper, name='subscribe_paper'),
	url(r'^mysubscription/$', subscription, name='subscription'),
	url(r'^unsubscribe/(?P<id>\d+)/$', unsubscribe, name='unsubscribe'),
	url(r'^subscription/$', subscription_details, name='mysubscription'),
	url(r'^edit/$', editsubscription, name='editsubscription'),
	url(r'^bill/$', Bill, name='bill'),
	url(r'^bill/(?P<paper>[\w -()]+)/$', paperbill, name='paperbill'),
	url(r'^account/$', allpapers, name='account'),
	url(r'^allbills/$', allbills, name='allbills'),

]
