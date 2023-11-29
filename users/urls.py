from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.authorization_api_view),
    path('register/', views.register),
    path('confirm/', views.verify),
]
