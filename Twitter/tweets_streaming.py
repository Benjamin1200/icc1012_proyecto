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

filename = "tweets_videogames_short.data"

# The information about the tweet to save as a tweet, for less space usage are:
# created_at, id, text, user[id], user[screen_name], user[location],
# user[followers_count], user[friends_count], user[favourites_count], user[statuses_count]

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def on_data(self, tweet):
        try:
            #print tweet
            values = json.loads(tweet)
            useful_values = {}
            for key in values:
                if key in ['id', 'created_at', 'text']:
                    useful_values.update({key: values[key]})
                if key == 'user':
                    useful_values.update({key: {}})
                    for secondary_key in values[key]:
                        if secondary_key in ['id', 'screen_name', 'location', 'followers_count', 'friends_count', 'favourites_count', 'statuses_count', 'created_at']:
                            useful_values[key].update({secondary_key: values[key][secondary_key]})
            #print useful_values
            with open(filename, 'a') as _file:
                #_file.write(tweet)
                _file.write(json.dumps(useful_values, sort_keys=True)+"\n")
        except:
            pass

    def on_error(self, status_code):
        print status_code
        return True  # Don't kill the stream

    def on_timeout(self):
        return True  # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=["Nintendo", "PlayStation", "Xbox", "Videogames"])
