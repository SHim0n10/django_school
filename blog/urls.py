from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_blog, name='vypis-blog'),
    path('kategorie/', views.vypis_kategorie, name='vypis-kategorie'),
    path('uzivatelia/', views.vypis_uzivatelov, name='vypis-uzivatelov')
]
