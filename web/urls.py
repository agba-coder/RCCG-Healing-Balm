from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('about-us/', views.about, name="about"),
    path('contact-us/', views.contact, name="contact"),
    path('prayer-requests/', views.prayer_request, name="prayer_request"),
    path('areas/children/', views.children, name="children"),
    # path('favicon.ico', lambda _ : redirect('static/assets/img/favicon.ico', permanent=True)),
]