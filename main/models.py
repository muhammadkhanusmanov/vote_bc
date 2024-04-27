from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    poll_que = models.CharField(max_length=300)
    candidates = models.ManyToManyField(User,related_name='candidate')

    def __str__(self):
        return f'{self.poll_que[:12]}...'

class Poll(models.Model):
    poll_que = models.CharField(max_length=300)
    que1 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que2 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que3 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que4 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que5 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que6 = models.CharField(max_length=150, blank=True, null=True, default=None)
    que7 = models.CharField(max_length=150, blank=True, null=True, default=None)