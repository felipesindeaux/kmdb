from django.urls import path

from genres.views import GenreView

urlpatterns = [
    path('genres/', GenreView.as_view())
]
