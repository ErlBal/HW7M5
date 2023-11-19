from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, \
ReviewSerializer, ReviewDetailSerializer


@api_view(['GET'])
def get_director(request):
    director = Director.objects.all()

    serializer = DirectorSerializer(director, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_director_id(request, director_id):
    director = Director.objects.get(id=director_id)

    serializer = DirectorDetailSerializer(director, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def get_movie(request):
    movie = Movie.objects.all()

    serializer = MovieSerializer(movie, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_movie_id(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    serializer = MovieDetailSerializer(movie, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def get_review(request):
    review = Review.objects.all()

    serializer = ReviewSerializer(review, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_review_id(request, review_id):
    review = Review.objects.filter(id=review_id)

    serializer = ReviewDetailSerializer(review, many=False)

    return Response(serializer.data)

