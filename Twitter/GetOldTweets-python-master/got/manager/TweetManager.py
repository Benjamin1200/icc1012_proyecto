import urllib,urllib2,json,re,datetime,sys,cookielib
from .. import models
from pyquery import PyQuery
import time

class TweetManager:

    def __init__(self):
        pass

    @staticmethod
    def getTweets(tweetCriteria, receiveBuffer = None, bufferLength = 100):
        refreshCursor = ''

        results = []
        resultsAux = []
        cookieJar = cookielib.CookieJar()

        if hasattr(tweetCriteria, 'username') and (tweetCriteria.username.startswith("\'") or tweetCriteria.username.startswith("\"")) and (tweetCriteria.username.endswith("\'") or tweetCriteria.username.endswith("\"")):
            tweetCriteria.username = tweetCriteria.username[1:-1]

        if hasattr(tweetCriteria, 'skip_tweets'):
            skip_tweets = tweetCriteria.skip_tweets

        active = True
        error_counter = 0

        while active:
            json = TweetManager.getJsonReponse(tweetCriteria, refreshCursor, cookieJar)

            error = False

            if json is None:
                print "Error happened with retrieval from twitter. Retrying in 1 minute..."
                error = True
                time.sleep(60)
                error_counter += 1
            
            if not error:
                if len(json['items_html'].strip()) == 0:
                    print "Empty response! Retrying in 1 minute..."
                    error = True
                    time.sleep(60)
                    error_counter += 1

            if not error:
                refreshCursor = json['min_position']
                tweets = PyQuery(json['items_html'])('div.js-stream-tweet')
                if len(tweets) == 0:
                    print "No new tweets found! Retrying in 1 minute..."
                    error = True
                    time.sleep(60)
                    error_counter += 1

            if error_counter > 10:
                print "There has been a lot of error! ({}) Saving data obtained to file.".format(error_counter)
                active = False

            if not error:
                for tweetHTML in tweets:
                    if skip_tweets == 0:
                        tweetPQ = PyQuery(tweetHTML)
                        tweet = models.Tweet()

                        try:
                            usernameTweet = tweetPQ("span.username.js-action-profile-name b").text();
                            txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text().replace('# ', '#').replace('@ ', '@'));
                            #retweets = int(tweetPQ("span.ProfileTweet-action--retweet span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""));
                            #favorites = int(tweetPQ("span.ProfileTweet-action--favorite span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""));
                            dateSec = int(tweetPQ("small.time span.js-short-timestamp").attr("data-time"));
                            id = tweetPQ.attr("data-tweet-id");
                            user_id = tweetPQ.attr("data-user-id");
                            permalink = tweetPQ.attr("data-permalink-path");

                            #geo = ''
                            #geoSpan = tweetPQ('span.Tweet-geo')
                            #if len(geoSpan) > 0:
                            #    geo = geoSpan.attr('title')
                        except:
                            error = True

                        if not error:
                            tweet.id = id
                            tweet.permalink = 'https://twitter.com' + permalink
                            tweet.username = usernameTweet
                            tweet.user_id = user_id
                            tweet.text = txt
                            tweet.date = datetime.datetime.fromtimestamp(dateSec)
                            #tweet.retweets = retweets
                            #tweet.favorites = favorites
                            #tweet.hashtags = " ".join(re.compile('(#\\w*)').findall(tweet.text))
                            #tweet.geo = geo

                            results.append(tweet)
                            resultsAux.append(tweet)
    
                                if receiveBuffer and len(resultsAux) >= bufferLength:
                                    receiveBuffer(resultsAux)
                                    resultsAux = []
    
                                if tweetCriteria.maxTweets > 0 and len(results) >= tweetCriteria.maxTweets:
                                    active = False
                                break

                    else:
                        skip_tweets -= 1

        if receiveBuffer and len(resultsAux) > 0:
            receiveBuffer(resultsAux)

        return results

    @staticmethod
    def getJsonReponse(tweetCriteria, refreshCursor, cookieJar):
        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"

        urlGetData = ''
        if hasattr(tweetCriteria, 'username'):
            urlGetData += ' from:' + tweetCriteria.username

        if hasattr(tweetCriteria, 'since'):
            urlGetData += ' since:' + tweetCriteria.since

        if hasattr(tweetCriteria, 'until'):
            urlGetData += ' until:' + tweetCriteria.until

        if hasattr(tweetCriteria, 'querySearch'):
            urlGetData += ' ' + tweetCriteria.querySearch

        if hasattr(tweetCriteria, 'topTweets'):
            if tweetCriteria.topTweets:
                url = "https://twitter.com/i/search/timeline?q=%s&src=typd&max_position=%s"

        try:
        	url = url % (urllib.quote(urlGetData), refreshCursor)
        except:
        	print "Error with urllib making the url."
        	return None

        headers = [
            ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]

        try:
        	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        	opener.addheaders = headers
        except:
        	print "Error with urllib2 (connection issues probably)."
        	return None

        try:
            response = opener.open(url)
            jsonResponse = response.read()
        except:
            print "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd" % urllib.quote(urlGetData)
            #sys.exit()
            return None

        try:
        	dataJson = json.loads(jsonResponse)
        except:
        	print "Error on trying to parse it as json."
        	return None

        return dataJson