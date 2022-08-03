from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'date_joined', 'updated_at']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class CriticSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']
