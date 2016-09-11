import json
import pymongo

filename = "tweets_videogames.data"
db = pymongo.MongoClient().project
_file = open(filename, 'r')
for line in _file.readlines():
    print line
    #db.tweets.insert(json.loads(line))
_file.close()
