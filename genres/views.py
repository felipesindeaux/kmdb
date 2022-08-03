from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreView(APIView):
    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)

        return Response(serializer.data)

    def post(self, request):
        
        serializer = GenreSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
