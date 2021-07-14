from tweets.serializers import TweetSerializer
from rest_framework.serializers import Serializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, permissions
from .models import Comment, Retweet, Tweet, Like
from .serializers import Commentserializer, LikeSerializer,Retweetserializer


# Create your views here.
def index(request):
    return HttpResponse("Hello Liberty")

class TweetViewSet(viewsets.ModelViewSet):
    '''
    Api endpoint taha allows user to be viewed or edited
    '''
    queryset=Tweet.objects.all()
    serializer_class = TweetSerializer

class LikeViewSet(viewsets.ModelViewSet):
    '''
    API that allows viewers to like 
    '''
    queryset=Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes= [permissions.IsAuthenticated]

class RetweetviewSet(viewsets.ModelViewSet):
    '''
    API for to save all retweets in the database 
    '''
    queryset=Retweet.objects.all()
    serializer_class = Retweetserializer


class CommentviewSet(viewsets.ModelViewSet):
    '''
    API for all trends available in the app 
    '''
    queryset = Comment.objects.all()
    serializer_class=Commentserializer


# class TrendsviewSet(viewsets.ModelViewSet):
#     '''
#     API for all trends available in the app 
#     '''
#     queryset=Trends.objects.all()
#     serializer_class=Trendsserializer