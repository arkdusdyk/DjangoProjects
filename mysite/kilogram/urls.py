from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'kilogram'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(),name = 'index'),
]#Generic view사용 (function view대신)
from django.contrib.auth.decorators import login_required
urlpatterns += [
	url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name = 'profile'),
	url(r'^profile_update/$', login_required(views.ProfileUpdateView.as_view()), name = 'profile_update'),
]