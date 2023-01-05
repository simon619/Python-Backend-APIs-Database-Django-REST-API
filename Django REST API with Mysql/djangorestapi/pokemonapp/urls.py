from django.urls import re_path
from pokemonapp import views

urlpatterns = [
    re_path(r'^pokemon$', views.pokemonApi),
    re_path(r'^pokemon/([0-9]+)$', views.pokemonApi),

    re_path(r'^trainer$', views.trainerApi),
    re_path(r'^trainer/([0-9]+)$', views.trainerApi),

]