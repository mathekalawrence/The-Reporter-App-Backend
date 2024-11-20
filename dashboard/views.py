from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework import filters

from users.serializers import *
from reports.serializers import *


class UsersListApiView(ListAPIView):
    """
    lists all users
    """
    permission_classes = [IsAdminUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class ReportsListApiView(ListAPIView):
    """
    lists all reports
    """
    permission_classes = [IsAdminUser]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ] 
