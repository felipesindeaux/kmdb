from django.urls import path

from users.views import LoginView, RegisterView, UserView, UserViewById

urlpatterns = [
    path('users/register/', RegisterView.as_view()),
    path('users/login/', LoginView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:id>/', UserViewById.as_view())
]
