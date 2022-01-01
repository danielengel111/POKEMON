from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.query_results, name='home'),
    path('', views.add_pokemon, name='home')
]
