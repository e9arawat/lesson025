from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('signup', views.signup, name='signup'),
    path('sign_out', views.sign_out, name="sign_out"),
    path('add_contact', views.add_contact, name='add_contact'),
    path('home', views.home, name='home'),
]