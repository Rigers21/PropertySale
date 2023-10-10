from django.urls import path
from properties import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<slug>/', views.detail, name='detail'),
]
