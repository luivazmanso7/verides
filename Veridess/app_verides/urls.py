
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contribuir/', views.contribuir, name='contribuir'),
    path('inscricao/', views.inscricao, name='inscricao'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contato/', views.contato, name='contato'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('confirmacao/', views.confirmacao, name='pagina_de_confirmacao'),
    path('faq/', views.faq_page, name='faq_page'),
    path('produto/<int:id>/', views.produto_detalhes, name='produto_detalhes'),
]




