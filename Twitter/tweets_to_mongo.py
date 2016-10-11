import json
import pymongo
import os

# Last insertion to mongodb: 11/10/2016

script_dir = os.path.dirname(__file__) #absolute dir the script is in
name_directory_old_tweets = "GetOldTweets-python-master/"

filenames = []
old_nintendo_filenames = []
old_playstation_filenames = []
old_xbox_filenames = []
old_videogames_filenames = []
old_nintendo_common_filename = name_directory_old_tweets + "old_tweets_short_nintendo_{}.data"
old_playstation_common_filename = name_directory_old_tweets + "old_tweets_short_playstation_{}.data"
old_xbox_common_filename = name_directory_old_tweets + "old_tweets_short_xbox_{}.data"
old_videogames_common_filename = name_directory_old_tweets + "old_tweets_short_videogames_{}.data"
filename_dates = ["2016-07-01", "2016-07-08", "2016-07-15", "2016-07-22", "2016-07-29", "2016-08-05",
                  "2016-08-12"]
""", "2016-08-19", "2016-08-26", "2016-09-02", "2016-09-09", "2016-09-16",
                  "2016-09-23" """
for i in xrange(0, len(filename_dates)):
    old_nintendo_filenames.append(os.path.join(script_dir, old_nintendo_common_filename.format(filename_dates[i])))
    old_playstation_filenames.append(os.path.join(script_dir, old_playstation_common_filename.format(filename_dates[i])))
    old_xbox_filenames.append(os.path.join(script_dir, old_xbox_common_filename.format(filename_dates[i])))
    old_videogames_filenames.append(os.path.join(script_dir, old_videogames_common_filename.format(filename_dates[i])))

filenames += old_nintendo_filenames + old_playstation_filenames + old_xbox_filenames + old_videogames_filenames
filenames.append(os.path.join(script_dir, "tweets_videogames.data"))
filenames.append(os.path.join(script_dir, "tweets_videogames_short.data"))

db = pymongo.MongoClient().project_tweets

# Sentence to run on mongo console:
# db.project_tweets.createIndex({"id": 1}, {unique: true})

for filename in filenames:
    _file = open(filename, 'r')
    for line in _file.readlines():
        data = json.loads(line)
        try:
            db.project_tweets.insert(data)
        except:
            print "Tweet was already in database."
    _file.close()
