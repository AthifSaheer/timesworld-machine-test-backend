from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_over_view, name='api_over_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('login/', obtain_auth_token),
    path('user/details/<str:token>/', views.user_details, name='user_details'),
]
