from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    # path('favicon.ico', lambda _ : redirect('static/assets/img/favicon.ico', permanent=True)),
]