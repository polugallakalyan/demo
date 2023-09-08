"""
URL configuration for project23 project.

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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topics/',display_topics,name='display_topics'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_accessrecord/',display_accessrecord,name='display_accessrecord'),
    path('insert_topics/',insert_topics,name='insert_topics'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_AccessRecord/',insert_AccessRecord,name='insert_AccessRecord'),
    path('update_webpage/',update_webpage,name='update_webpage'),
]
