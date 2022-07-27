"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static


# from django.conf import global_settings
# from conf import settings
#settings를 가져올때는 global_settings를 오버라이딩해서 가져와야 하기 때문에 
#다음과 같이 import 해온다. 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('django_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# settings.MEDIA_URL
# settings.MEDIA_ROOT
