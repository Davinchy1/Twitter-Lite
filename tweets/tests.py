from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Comment, Like, Tweet, Retweet

class TweetTests(APITestCase):
    def test_create_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")

        url = reverse('tweet-list')
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

    def test_put_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'For this Lagos?', "user": user.id, "tweet": tweet.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Tweet.objects.count(), 1)
        # self.assertEqual(Tweet.objects.get().text, data['text'])
        # self.assertEqual(response_data['text'], data['text'])


    def test_patch_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="it's a testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'For this Lagos?', "user": user.id, "tweet": tweet.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="File! issa testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        # data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.count(), 1)
        # self.assertEqual(response_data[0]["text"], tweet.text)


    def test_get_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        # data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="testing game", user=user)

        url = reverse('tweet-detail', kwargs={'pk': tweet.id})
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RetweetTests(APITestCase):
    def test_create_retweet(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_retweet(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_retweet(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="testing game ", user=user)
        retweet = Retweet.objects.create(user=user, tweet=tweet)

        url = reverse('retweet-detail', kwargs={"pk":retweet.id})
        # data = {'text': 'DabApps', "user": user.id, "tweet": tweet.id, "retweet": retweet.id }
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class LikeTests(APITestCase):
    def test_create_like(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="created tweet", user=user)

        url = reverse('like-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_like(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="my own tweet", user=user)

        url = reverse('like-list')
        response = self.client.get(url, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1like(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="django don loud ooo!!!", user=user)

        url = reverse('like-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_like(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="created tweet", user=user)
        like = Like.objects.create(user=user, tweet=tweet)

        url = reverse('like-detail', kwargs={"pk": like.id})
        # data = {'tweet': tweet.id, "like": like.id}
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentTests(APITestCase):
    def test_create_comment(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="this is a comment", user=user)

        url = reverse('comment-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_comment(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_comment(self):
        """
        Ensure we can GET a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        tweet = Tweet.objects.create(text="created tweet", user=user)
        comment = Comment.objects.create(user=user, tweet=tweet, text="e go better!")

        url = reverse('comment-detail', kwargs={"pk": comment.id})
        # data = {'tweet': tweet.id, "like": like.id}
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
