from django.urls import path

from movies.views import MovieView, MovieViewById

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:id>/', MovieViewById.as_view())
]
