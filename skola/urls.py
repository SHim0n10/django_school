from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name='triedy'),
    path('ucitelia/', views.vypis_ucitelia, name='ucitelia'),
    path('ucitelia/<ucitel>/', views.vypis_ucitel, name='ucitel'),
    path('studenti/', views.vypis_studenti, name='studenti'),
    path('studenti/<student>/', views.vypis_student, name='student'),
    path('triedy/<trieda>/', views.vypis_trieda, name='trieda'),
    path('kruzky/', views.vypis_kruzky, name='kruzky'),
    path('kruzky/<kruzok>/', views.vypis_kruzok, name='kruzok'),
    path('uzivatel/pridat/', views.pridat_uzivatel, name='pridat_uzivatel'),
    path('uzivatel/pridat2/', views.pridat_uzivatel2, name='pridat_uzivatel2'),
]
