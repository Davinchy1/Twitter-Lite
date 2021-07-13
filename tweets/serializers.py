from django.db.models import fields
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Comment, Retweet, Trends, Tweet, Like

class TweetSerializer(ModelSerializer):
    likes = IntegerField(source="get_num_like",read_only = True)
    retweet = IntegerField(source="get_num_retweet",read_only =True)
    comment = IntegerField(source="get_num_comment",read_only=True)
    username = CharField(source="user.username",read_only=True)
    class Meta:
        model = Tweet
        fields =["text", "likes","retweet","created_on","comment","username", "user"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["tweet", "user"]

class Retweetserializer(ModelSerializer):
    class Meta:
        model = Retweet
        fields = ["tweet", "user"]
        # depth = 1

class Trendsserializer(ModelSerializer):
    class Meta:
        model = Trends
        fields = ["tweet", "user"]

class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["tweet","user"]