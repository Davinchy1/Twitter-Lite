from tweets.models import Comment
from django.db import router
# from posts.views import my_view
from rest_framework import routers
from django.urls.conf import include
from django.urls import path
from tweets.views import TweetViewSet, LikeViewSet, RetweetviewSet, CommentviewSet, index


router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'retweet',RetweetviewSet)
# router.register(r'trends',TrendsviewSet)
router.register(r"comment",CommentviewSet)


urlpatterns = [
    path('index/', index),
    path("", include(router.urls))
]
