from django.urls import path
from movie_app import views


urlpatterns = [
    path('director/', views.get_director),
    path('director/<int:director_id>/', views.get_director_id),
    path('movie/', views.get_movie),
    path('movie/<int:movie_id>/', views.get_movie_id),
    path('review/', views.get_review),
    path('review/<int:review_id>/', views.get_review_id)
]