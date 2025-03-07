from django.shortcuts import render

from rest_framework import generics
from models import Analysis
from serializers import AnalysisSerializer

class AnalysisDetailAPIView(generics.RetrieveAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer