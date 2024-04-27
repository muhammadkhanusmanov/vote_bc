from django.db import models
from django.contrib.auth.models import User


class Polls(models.Model):
    poll_que = models.CharField(max_length=300)
    que1 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que2 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que3 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que4 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que5 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que6 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que7 = models.CharField(max_length=150, blank=True, null=True, default=None)
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll_que

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE,related_name='votes')
    answer = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username

