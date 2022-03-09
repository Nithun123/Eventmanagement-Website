from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [

    path('',views.login),
    path('signin/',views.signin),
    path('signup/',views.signups),
    path('dashboard',views.dashboard),
    path('show',views.shows),
    path('detail',views.deatils),
    path('details/',views.dshow),
    path('contact',views.contacts),
    path('about/',views.about),
    path('add/',views.add),
    path('dele/<int:id>',views.delete),
    path('pay/',views.Pay)


]