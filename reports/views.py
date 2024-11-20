from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters

from .serializers import *


class ReportListCreateApiView(ListCreateAPIView):
    """
    creates or lists reports
    """
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]