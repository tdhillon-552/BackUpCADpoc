from django.contrib import admin
from django.urls import path, include
from BackUpDispatch import views

urlpatterns = [

    path('', views.home, name='BackUpDispatch_home'),

]
