from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserApiView.as_view()),    
    path('user/', UserApiView.as_view()),
]