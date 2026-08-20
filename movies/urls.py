from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("add/", views.movie_create, name="movie_create"),
    path("<int:pk>/edit/", views.movie_update, name="movie_update"),
    path("<int:pk>/delete/", views.movie_delete, name="movie_delete"),
    path("<int:pk>/toggle-watched/", views.toggle_watched, name="toggle_watched"),
]