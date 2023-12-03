from django.urls import path
from movie_app import views


urlpatterns = [
    path('director/', views.DirectorListCreateAPIView.as_view()),
    path('director/<int:director_id>/', views.DirectorIdRetrieveUpdateDestroyAPIView.as_view()),
    path('movie/', views.MovieListCreateAPIView.as_view()),
    path('movie/<int:id>/', views.MovieIdRetrieveUpdateDestroyAPIView.as_view()),
    path('review/', views.ReviewListCreateAPIView.as_view()),
    path('review/<int:id>/', views.ReviewIdRetrieveUpdateDestroyAPIView.as_view())
]