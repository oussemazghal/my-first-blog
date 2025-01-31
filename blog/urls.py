from django.urls import path
from . import views  # Importation des vues

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Page d'accueil du blog
]
