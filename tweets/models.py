from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
