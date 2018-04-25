from django.conf.urls import url
from .views import show_topics,show_all

urlpatterns = [
	url(r'^genre/(?:(?P<name>[\w.@+-]+))/$', show_topics, name='show_topic'),
	url(r'^$',show_all,name='show_all')
]
