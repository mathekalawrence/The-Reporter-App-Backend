from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from .models import *
from .utils import create_user_otp


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    full_name = serializers.CharField(
        required=True
    )
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password fields didn't match.")

    def create(self, validated_data):
        otp = create_user_otp()
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            otp_code=otp
        )
        password = validated_data['password']
        user.save()
        user.update_user_password(password)
        return user
    
