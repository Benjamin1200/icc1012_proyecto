import json
import pymongo
import tweepy
import sys
import psycopg2

#Variables that contains the user credentials to access Twitter API
access_key = "78137173-XJvAwl9VadKIZdRCxdDuQOdZDIW4LZZ6nHBeJCMCk"
access_secret = "7Dbyhbdk0HVyKaZOondUeVXd29K92kXddDlBRkHN2CdTQ"
consumer_key = "LTQHIMQH8e2G0bNTHfhXp0iJp"
consumer_secret = "PW51HWMv70ALtBzPA1g5KrCKyIr5zcCEWv4JdyqCVTfnV5zHO0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
	self.count = 1
	self.Max = 2
        self.db = pymongo.MongoClient().prueba

    def on_data(self, tweet):
	text =  json.loads(tweet)["text"]
	RT = text[0:4] == "RT @" 
	lang = json.loads(tweet)["lang"]
	created_at = json.loads(tweet)["created_at"] 
	latitude = 0
	longitude = 0
	country = "None";
	if str(json.loads(tweet)["place"]) != "None":
		country =  json.loads(tweet)["place"]["country"]
	self.db.tweet.insert(json.loads(tweet))
	self.count += 1
	sys.exit()

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['Rio'])
