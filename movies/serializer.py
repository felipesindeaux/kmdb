from dataclasses import fields

from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)
    
    class Meta():
        model = Movie
        fields = "__all__"
        read_only_fields = ['id']

    def create(self, validated_data):

        print(validated_data)

        genres = validated_data.pop('genres')

        validated_genres = [Genre.objects.get_or_create(**genre)[0] for genre in genres]

        created_movie = Movie.objects.create(**validated_data)

        for genre in validated_genres:
            genre.movies.add(created_movie)

        return created_movie
    
    def update(self, instance, validated_data):
        if validated_data.get('genres', None):
            new_genres = validated_data.pop('genres')
            old_genres = instance.genres.all()

            validated_genres = [Genre.objects.get_or_create(**genre)[0] for genre in new_genres]

            instance.genres.set([*old_genres, *validated_genres])
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
