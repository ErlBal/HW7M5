from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='director name')

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=80, verbose_name='movie title')
    description = models.CharField(max_length=200, verbose_name='movie description')
    duration = models.CharField(max_length=100, verbose_name='movie duration')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movie_director')

    def __str__(self):
        return f'{self.title}, {self.director}'

class Review(models.Model):
    STARS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    text = models.CharField(max_length=400, verbose_name='review text')
    rate_stars = models.IntegerField(choices=STARS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
