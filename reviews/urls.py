from django.urls import path

from reviews.views import ReviewView, ReviewViewById

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', ReviewViewById.as_view()),
    path('reviews/<int:review_id>/', ReviewViewById.as_view()),
    path('reviews/', ReviewView.as_view())
]
