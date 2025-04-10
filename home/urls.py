"""AutomaticAnswerChecker URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    # path('home/',views.home, name='home'),
    path('test/',views.test, name="test"),
    path('start/',views.start, name="start"),
    path('',views.mjc, name="mjc"),
    path('mjc/',views.mjc, name="mjc"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('instruction/',views.instruction, name="instruction"),
    path('logout/',views.logout, name="logout"),
]


