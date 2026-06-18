from django.urls import path
from apps.users.views import  LoginView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
]