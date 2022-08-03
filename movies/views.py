from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, status

from movies.models import Movie
from movies.permissions import MoviesPermission
from movies.serializer import MovieSerializer


class MovieView(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviesPermission]

    def get(self, request):
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieViewById(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviesPermission]

    def get(self, request, id):

        movie = get_object_or_404(Movie, pk=id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def patch(self, request, id):
        movie = get_object_or_404(Movie, pk=id)

        serializer = MovieSerializer(movie, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, id):
        movie = get_object_or_404(Movie, pk=id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

