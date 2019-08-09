from django.urls import path

from demo_app import views

app_name = 'demo_app'

urlpatterns = [
    path('', views.index),
    path('save_news/', views.save_news, name='save_news'),
]
