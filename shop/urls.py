from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_shop, name='vypis-shop'),
    path('kategorie/', views.vypis_kategorie, name='vypis-kategorie'),
    path('produkty/', views.vypis_produkty, name='vypis-produkty'),
    path('uzivatelia/', views.vypis_uzivatelov, name='vypis-uzivatelov'),
    path('objednavky/', views.vypis_objednavky, name='vypis-objednavky'),
    path('kategorie/<kategoria>/', views.vypis_kategoriu, name='kategoria'),
    path('produkty/<produkt>/', views.vypis_produkt, name='produkt'),
]
