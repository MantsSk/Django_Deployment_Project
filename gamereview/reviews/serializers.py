
from rest_framework import serializers
from .models import GameReview


class GameReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.id')

    class Meta:
        model = GameReview
        fields = ['id', 'game', 'reviewer',
                  'content', 'date_created', 'rating']
