from rest_framework import serializers

from reviews.models import Review
from users.serializers import CriticSerializer


class ReviewSerializer(serializers.ModelSerializer):

    critic = CriticSerializer(required=False)

    class Meta():
        model = Review
        fields = "__all__"
        read_only_fields = ["id", "movie"]
        extra_kwargs = {"stars": {"min_value": 1, "max_value": 10}}

    def create(self, validated_data):
        user = self.context.get('user')
        movie = self.context.get('movie')
        
        validated_data['critic'] = user
        validated_data['movie'] = movie

        created_review = Review.objects.create(**validated_data)

        return created_review
        
