import json
import tweepy

# Variables that contains the user credentials to access Twitter API
access_key = "766667542240882688-NtPIOdl9CCKLZ7UBn8JaLIiJ6k3wYQN"
access_secret = "RYWpbnHH3cbh7R7MXs8qVzgGwTBAcPn79IYeXISGvEiHO"
consumer_key = "GU8slDLVo4HygqL15RCVfQWd0"
consumer_secret = "Tlp6rArgxhGrySTrbSfgKgCyA2UUf4x41UEDYu3OaOG9ZEccGY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filename = "tweets_videogames.data"

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def on_data(self, tweet):
        print tweet
        values = json.loads(tweet)
        try:
            with open(filename, 'a') as _file:
                _file.write(tweet)
        except:
            pass

    def on_error(self, status_code):
        return True  # Don't kill the stream

    def on_timeout(self):
        return True  # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=["Nintendo", "PlayStation", "Xbox", "Videogames"])
