"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView, RedirectView
from .views import *

urlpatterns = [
    path('enter/', enter, name='enter'),
    re_path(r'^ulogout/', ulogout, name='ulogout'),
    path('regist/', regist, name='regist'),
    re_path(r'^main/', MainView.as_view(), name='main'),
    path('schedule/', schedule, name='schedule'),
    path('', RedirectView.as_view(url='main/')),
    path('admin/', admin.site.urls),
    path('gallery/', PhotoUpload, name='gallery'),
    # path('success', success, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
