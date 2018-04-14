"""beta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import home.views
import users.views
import contact.views
import newspapers.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('users.urls')),
    url(r'^details/',include('news_subscription.urls')),
    url(r'^vendor/',include('user_vendor.urls')),
    url(r'^pincode/',include('pincode.urls')),
    url(r'^vendor-admin/',include('Vendor.urls')),
    url(r'^genres/',include('dailydigest.urls',namespace='genreee')),
    url(r'^$',home.views.Home, name="home"),
    url(r'^explore/$',home.views.Home2, name="home2"),
    url(r'^contact-us$', home.views.contact, name="contact"),
    url(r'^faqs$', home.views.faqs, name="faqs"),
    url(r'^accounts$', home.views.account, name="account"),
    url(r'^about$', home.views.about, name="about"),
    url(r'^workwithus$', home.views.workwithus, name="workwithus"),
    url(r'^privacy-policy$',home.views.privacy, name="privacy"),
    url(r'^welcome/$',home.views.welcome, name="welcome"),
    url(r'^dummy/$',home.views.dummy, name="dummy"),
    url(r'^newsletter/$',contact.views.newsletter_entry, name="newsletter"),
    url(r'^contact/$',contact.views.contact_entry, name="contact_entry"),
    url(r'^work/$',contact.views.work_entry, name="work"),
    url(r'^newspapers/$',newspapers.views.all_newspapers, name="all_newspapers"),
    url(r'^req-contact/$',home.views.req_contact, name="req_contact"),

    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT) 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)