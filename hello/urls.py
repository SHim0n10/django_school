from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('world/', views.hello_world, name='hello-world'),
    path('<slovo>/', views.slovo, name='slovo')
]
