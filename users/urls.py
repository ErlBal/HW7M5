from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
    path('confirm/', views.ConfirmAPIView.as_view()),
]
