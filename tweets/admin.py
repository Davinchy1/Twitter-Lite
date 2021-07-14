from tweets.models import Tweet
from tweets.models import Retweet
from tweets.models import Comment
from tweets.models import Like

from django.contrib import admin

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Retweet)
admin.site.register(Comment)
# admin.site.register(Trends)
