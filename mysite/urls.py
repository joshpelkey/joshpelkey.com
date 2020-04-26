"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from mysite.views import welcome, eighteen_playlist, welcome_college, anna_gray_college, clara_jayne_college

urlpatterns = [
	url(r'^$', welcome),
	url(r'^529/$', welcome_college),
	url(r'^529/anna$', anna_gray_college),
	url(r'^529/clara$', clara_jayne_college),
	url(r'^18playlist$', eighteen_playlist),
]
