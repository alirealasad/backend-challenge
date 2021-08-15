from django.urls import path
from .views import LoginView, UserView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
]
