from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, \
ReviewSerializer, ReviewDetailSerializer


@api_view(['GET', 'POST'])
def get_director(request):
    if request.method == 'GET':
        director = Director.objects.all()

        serializer = DirectorSerializer(director, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
            name=name
        )

        serializer = DirectorSerializer(director, many=True)

        return Response(
            {
                "message": "succes",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_director_id(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response({f"Director with id {director_id} don't exist"}, status=404)

    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        director.name = request.data.get('name', director.name)

        director.save()

        serializer = DirectorDetailSerializer(instance=director, many=False)

        return Response(
            data={
                "message": "updated",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE':
        director.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )

@api_view(['GET', 'POST'])
def get_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
        )

        serializer = MovieSerializer(movie, many=True)

        return Response(
            {
                "message": "succes",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_id(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({f"Movie with id {news_id} don't exist"}, status=404)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie.title = request.data.get('title', movie.title)
        movie.description = request.data.get('description', movie.description)
        movie.duration = request.data.get('duration', movie.duration)


        movie.save()

        serializer = MovieDetailSerializer(instance=movie, many=False)

        return Response(
            data={
                "message": "updated",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE':
        movie.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )


@api_view(['GET', 'POST'])
def get_review(request):
    if request.method == 'GET':
        review = Review.objects.all()

        serializer = ReviewSerializer(review, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        rate_stars = request.data.get('rate_stars')
        movie = request.data.get('movie')

        review = Review.objects.create(
            text=text,
            rate_stars=rate_stars,
            movie=movie
        )

        serializer = ReviewSerializer(review, many=True)

        return Response(
            {
                "message": "succes",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_review_id(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({f"Review with id {news_id} don't exist"}, status=404)

    if request.method == 'GET':
        serializer = ReviewDetailSerializerSerializer(review, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
       text = request.data.get('text', review.text)
       rate_stars = request.data.get('rate_stars', review.rate_stars)
       movie = request.data.get('movie', review.movie)

       review.save()

       serializer = MovieDetailSerializer(instance=review, many=False)

       return Response(
           data={
               "message": "updated",
               "data": serializer.data
           },
           status=200
       )

    if request.method == 'DELETE':
        review.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )



