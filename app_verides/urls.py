from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contribuir/', views.contribuir, name='contribuir'),
    path('inscricao/', views.inscricao, name='inscricao'),
    path('doacoes/', views.doacoes, name='doacoes'),
]