from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, \
ReviewSerializer, ReviewDetailSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def get_director(request):
    if request.method == 'GET':
        director = Director.objects.all()

        serializer = DirectorSerializer(director, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director = serializer.save()

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
        serializer = DirectorValidateSerializer(instance=news, data=request.data)
        serializer.is_valid(raise_exception=True)
        news = serializer.update(instance=director, validated_data=serializer.validated_data)

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
@permission_classes([IsAuthenticated])
def get_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()

        serializer = MovieSerializer(movie, many=True)

        return Response(
            {
                "message": "succes",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_movie_id(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({f"Movie with id {news_id} don't exist"}, status=404)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieValidateSerializer(instance=news, data=request.data)
        serializer.is_valid(raise_exception=True)
        news = serializer.update(instance=movie, validated_data=serializer.validated_data)

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
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

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
        serializer = ReviewValidateSerializer(instance=news, data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.update(instance=news, validated_data=serializer.validated_data)

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



