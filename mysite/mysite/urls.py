"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from kilogram import views as kilogram_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',kilogram_views.IndexView.as_view(), name = 'root'),
    path('admin/', admin.site.urls),
    url(r'^kilogram/', include('kilogram.urls')),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/signup$', kilogram_views.CreateUserView.as_view(), name ="signup"),
	url(r'^accounts/signup/done$', kilogram_views.RegisteredView.as_view(), name = "create_user_done"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)	#정적으로 추가할 URL = MEDIA_URL이고 실제는 settings.MEIDA_ROOT에 있다
