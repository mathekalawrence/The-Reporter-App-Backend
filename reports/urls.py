from django.urls import path
from .views import *

urlpatterns = [
    path('', ReportListCreateApiView.as_view())
]