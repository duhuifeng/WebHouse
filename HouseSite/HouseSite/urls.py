"""HouseSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path,include
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
from apps.users import views
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

API_TITLE = 'API DOCUMENT'
API_DESCRIPTION = 'BASIC API DOCUMENT'

urlpatterns = [
    url(r'v1/report/$', views.DeviceReport.as_view(), name='DeviceReport'),
    url(r'docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, authentication_classes=[], permission_classes=[])), #api参考文档
    path('admin/', xadmin.site.urls), #管理员界面
]