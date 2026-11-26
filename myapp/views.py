from rest_framework import generics
from rest_framework.exceptions import ValidationError

from api.score_filter import parse_score_filter
from .models import Review
from .serializers import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """Optionally filter reviews by a finite numeric score threshold."""
        queryset = Review.objects.all()
        try:
            score = parse_score_filter(self.request.query_params.get("score"))
        except ValueError as error:
            raise ValidationError({"score": str(error)}) from error

        if score is not None:
            queryset = queryset.filter(score__gte=score)
        return queryset
