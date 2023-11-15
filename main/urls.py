from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/director/', views.get_director),
    path('api/v1/director/<int:director_id>/', views.get_director_id),
    path('api/v1/movie/', views.get_movie),
    path('api/v1/movie/<int:movie_id>/', views.get_movie_id),
    path('api/v1/review/', views.get_review),
    path('api/v1/review/<int:review_id>/', views.get_review_id)
]
