from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Tweet(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    def get_num_like(self):
        return Like.objects.filter(tweet=self).count()
    
    def get_num_retweet(self):
        return Retweet.objects.filter(tweet=self).count()

    def get_num_comment(self):
        return Comment.objects.filter(tweet=self).count()
    
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tweet=models.ForeignKey(Tweet,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and twee pair dont occure more thand once
        #e.g(user1, tweet1) can only exit once 
        unique_together = ("user","tweet")
    

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and twee pair dont occure more thand once
        #e.g(user1, tweet1) can only exit once 
        unique_together = ("user","tweet",)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and tweet pair dont occure more thand once
        #e.g(user1, tweet1) can only exit once 
        unique_together = ("user","tweet")


# class Trends(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
#     created_on =models.DateTimeField(auto_now_add=True)