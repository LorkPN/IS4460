from django.contrib import admin
from django.urls import path
from .views import LoginView, MovieListView, MovieUpdateView, MovieDetailView, MovieAddView

urlpatterns = [
    path('login/', LoginView.as_view(), name='movie-login'),
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('update/<int:movie_id>/', MovieUpdateView.as_view(), name='movie-update'),
    path('update/', MovieUpdateView.as_view(), name='movie-update'),
    path('details/<int:movie_id>/', MovieDetailView.as_view(), name='movie-details'),
    path('details/', MovieDetailView.as_view(), name='movie-details'),
    path('add/', MovieAddView.as_view(), name='movie-add'),
]