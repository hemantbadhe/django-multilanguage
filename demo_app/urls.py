from django.contrib import admin
from django.urls import path

from demo_app import views

app_name = 'demo_app'

urlpatterns = [
    path('', views.index),
]
