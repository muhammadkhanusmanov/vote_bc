from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from .models import Polls, Vote
from django.contrib.auth.models import User


class PollSerializer(ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'