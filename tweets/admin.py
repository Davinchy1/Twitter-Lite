from tweets.models import Comment, Retweet, Tweet, Like, Trends
from django.contrib import admin

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Retweet)
admin.site.register(Trends)
admin.site.register(Comment)