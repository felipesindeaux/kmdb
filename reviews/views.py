from django.shortcuts import get_object_or_404, render
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination

from reviews.models import Review
from reviews.permissions import IsOwnerOrAdmin
from reviews.serializer import ReviewSerializer


class ReviewView(APIView, PageNumberPagination):

    def get(self, request):
        reviews = Review.objects.all()

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    

class ReviewViewById(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def get(self, request, movie_id):

        movie = get_object_or_404(Movie, pk=movie_id)

        reviews = Review.objects.filter(movie_id=movie_id)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request, movie_id):

        movie = get_object_or_404(Movie, pk=movie_id)
        
        serializer = ReviewSerializer(data=request.data, context={'movie': movie, 'user': request.user})

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        self.check_object_permissions(request, review.critic)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
