from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='director name')

class Movie(models.Model):
    title = models.CharField(max_length=80, verbose_name='movie title')
    description = models.CharField(max_length=200, verbose_name='movie description')
    duration = models.CharField(max_length=100, verbose_name='movie duration')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movie_director')

class Review(models.Model):
    text = models.CharField(max_length=400, verbose_name='review text')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
