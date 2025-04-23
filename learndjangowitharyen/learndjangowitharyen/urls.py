"""
URL configuration for learndjangowitharyen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('tweet_list/' , include('tweet.urls')),# "For anything that starts with /tweet_list/, go look in tweet/urls.py to find more routes."
    path('accounts/' , include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) # “this tells django Please serve files from MEDIA_ROOT when the browser asks for a URL starting with MEDIA_URL.”
