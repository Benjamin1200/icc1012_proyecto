import got
import json

def main():

    def printTweet(descr, t):
        print descr
        attributes = vars(t)
        for attribute in attributes.items():
            print attribute

    def save_tweet_as_dict(tweet):
        useful_values = {}
        useful_values.update({'user': {}})
        attributes = vars(tweet)
        keys = ['text', 'id', 'date', 'username', 'user_id', ]
        for attribute in attributes.items():
            if attribute[0] in keys:
                real_key = ""
                key = attribute[0]
                if key == "text" or key == "id":
                    real_key = key
                    useful_values.update({real_key: attribute[1]})
                elif key == "username":
                    real_key = "screen_name"
                    useful_values['user'].update({real_key: attribute[1]})
                elif key == "user_id":
                    real_key = "id"
                    useful_values['user'].update({real_key: attribute[1]})
                elif key == "date":
                    real_key = "created_at"
                    useful_values.update({real_key: attribute[1].strftime("%a %b %e %H:%M:%S +0000 %Y")})
        return useful_values

    date_since = "2016-07-15"
    date_until = "2016-07-22"
    wanted_tweets = 150000
    skip_tweets = 0

    filename = "old_tweets_short_playstation_{}.data".format(date_since)
    try:
        with open(filename, 'r') as _file:
            for line in _file.readlines():
                skip_tweets += 1
    except:
        print "No file found, to see tweets to skip."

    max_tweets = wanted_tweets - skip_tweets

    # Example 2 - Get tweets by query search
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('PlayStation').setSince(date_since).setUntil(date_until).setMaxTweets(max_tweets).skip_tweets(skip_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    for tweet in tweets:
        tweet_dict = save_tweet_as_dict(tweet)
        #print "DICT:", tweet_dict

        with open(filename, 'a') as _file:
            # _file.write(tweet)
            _file.write(json.dumps(tweet_dict, sort_keys=True) + "\n")


if __name__ == '__main__':
    main()
