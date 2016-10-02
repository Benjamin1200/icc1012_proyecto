import json
import pymongo

# TODO: read from different files, 3 so far (the full tweet data one, the short tweet data and the cursor data.
# TODO: verify that the tweet id is not already inside the mongoDB -> O(n)

filename = "tweets_videogames.data"
db = pymongo.MongoClient().project
_file = open(filename, 'r')
for line in _file.readlines():
    print line
    #db.tweets.insert(json.loads(line))
_file.close()
