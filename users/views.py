from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


def error_response_creator(error):
    """
    creates custom error message from serializer errors
    """
    error_data = {
        'success': False,
        'code': 'ERR_VALIDATION_ERROR',  
        'message': 'Validation error',
        'details': []
    }
    for field_name, error_messages in error.items():
        for error_message in error_messages:
            error_data['details'].append({
                'field': field_name,
                'message': str(error_message)
            })
    return error_data


class RegisterUserApiView(GenericAPIView):
    """
    registers a user to the platform
    """
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data['email'])
            data = {
                "message": "User created successfully",
                "otp": user.otp_code
            }
            return Response(data)
        else:
            data = error_response_creator(serializer.errors)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserApiView(GenericAPIView):
    """
    gets, updates and deletes user
    """
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            data = error_response_creator(serializer.errors)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        serializer = UsersSerializer(user)
        serializer_data = serializer.data
        user.delete()
        data = {
            "message": "Deleted User successfully",
            "user": serializer_data
        }
        return Response(data)