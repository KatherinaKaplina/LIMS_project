"""
URL configuration for LIMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import index
from main.views import main
from users.views import login, register, logout
from main.views import tracking
from main.views import reagent_changed
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index, name='index'),
    path('main/', main, name='main'),
    path('main/page/<int:page>/', main, name='page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('tracking/<int:reagent_id>', tracking, name='tracking'),
    path('logout/', logout, name='logout'),
    path('reagent_changed/<int:id>', reagent_changed, name='reagent_changed'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)