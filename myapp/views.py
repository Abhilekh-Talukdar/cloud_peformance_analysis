from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

from django.db.models import FloatField
from django.db.models.functions import Cast

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
        Optionally filter the queryset based on the 'score' parameter in the URL.
        """
        queryset = Review.objects.all()
        score = self.request.query_params.get('score', None)
        if score is not None:
            queryset = queryset.filter(score__gte=score)
        return queryset
