from rest_framework import serializers
from movie_app.models import Director, Movie, Review



class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'rating')

    def get_rating(self, obj):
        review_all = obj.movie_review.all()
        rate = [i.rate_stars for i in review_all]
        rate_avg = sum(rate) / len(rate)
        return rate_avg

class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')




class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'text', 'rate_stars')


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie')


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ('id', 'name', 'movie_count')

    def get_movie_count(self, obj):
        return obj.movie_director.count()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    description = serializers.CharField(max_length=200)
    duration = serializers.CharField(max_length=100)
    director_id = serializers.IntegerField()

    def validate_director_id(self, value: int):
        try:
            Director.objects.get(id=value)
        except Director.DoesNotExist:
            raise serializers.ValidationError('Director is not found')
        return value

    def validate_title(self, value):
        if len(value) < 0:
            raise serializers.ValidationError('length must be greater than zero')
        return value

    def validate_description(self, value):
        if len(value) < 50:
            raise serializers.ValidationError('length must be greater than fifty')
        return value

    def validate_duration(self, value):
        if len(value) < 200 or len(value) > 60:
            raise serializers.ValidationError('duration cannot be less than 60 or more than 200')

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        duration = validated_data.get('duration')
        director_id = validated_data.get('director_id')


        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.director_id = validated_data.get('director_id', instance.director_id)

        instance.save()

        return instance

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)


    def validate_name(self, value):
        if len(value) < 0:
            raise serializers.ValidationError('length must be greater than zero')
        return value

    def create(self, validated_data):
        name = validated_data.get('name')

        director = Director.objects.create(
            name=name
        )

        return director

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()

        return instance

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=40)
    rate_stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, value: int):
        try:
            Movie.objects.get(id=value)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Movie is not found')
        return value

    def validate_text(self, value):
        if len(value) < 0:
            raise serializers.ValidationError('length must be greater than zero')
        return value

    def validate_rate_stars(self, value):
        if len(value) < 5 or len(value) > 1:
            raise serializers.ValidationError('enter a number from 1 to 5')
        return value

    def create(self, validated_data):
        text = validated_data.get('text')
        rate_stars = validated_data.get('rate_stars')
        movie_id = validated_data.get('movie_id')

        review = Director.objects.create(
            text=text,
            rate_stars=rate_stars,
            movie_id=movie_id
        )

        return review

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.rate_stars = validated_data.get('rate_stars', instance.rate_stars)
        instance.movie_id = validated_data.get('movie_id', instance.movie_id)

        instance.save()

        return instance