from django.conf.urls import url
from .views import register,login,logout, profile_edit,loginuser,profile



urlpatterns = [
    url(r'^register/$', register, name='signup'),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    #url(r'^update_profile/$', profile_update, name = 'profile_update'),
    #url(r'^edit_profile/$', profile_edit, name = 'profile_edit'),
    url(r'^(?P<username>[\w.@+-]+)/profile/$', profile, name = 'profile'),
    url(r'^(?P<username>[\w.@+-]+)/$', loginuser, name = 'loginuser'),
    #url(r'^(?P<username>[\w.@+-]+)/update_profile/$',profile_update, name = 'update_profile'),
    url(r'^(?P<username>[\w.@+-]+)/edit_profile/$', profile_edit, name = 'edit_profile'),
]
