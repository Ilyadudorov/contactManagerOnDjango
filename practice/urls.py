"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from weather.views import *
from weather.views import categories
from contactManager.views import *
from practice import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('weather.urls')),
    path('', include('contactManager.urls')),
    path('contact/', include('contactManager.urls'))
]
#Этот кусок кода нужен для того чтоб пути для медиа файлов работали в дебаг режими, без дебаг режима все также будет работать
if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
handler404 = pageNotFound  #Данная переменная (название обязательное для django) вызывает функцию в urls (в том числе ищет в urls приложениях)
                           #при ошибке 404. То есть также можно сделать оработчик ошибки 500 (handler500) и так далее. 