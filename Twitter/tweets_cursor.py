import json
import tweepy
import datetime

# Variables that contains the user credentials to access Twitter API
access_key = "766667542240882688-NtPIOdl9CCKLZ7UBn8JaLIiJ6k3wYQN"
access_secret = "RYWpbnHH3cbh7R7MXs8qVzgGwTBAcPn79IYeXISGvEiHO"
consumer_key = "GU8slDLVo4HygqL15RCVfQWd0"
consumer_secret = "Tlp6rArgxhGrySTrbSfgKgCyA2UUf4x41UEDYu3OaOG9ZEccGY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filename = "tweets_videogames_test.data"
last_saved_tweet = None
max_amount_tweets = 10

# The information about the tweet to save as a tweet, for less space usage are:
# created_at, id, text, user[id], user[screen_name], user[location],
# user[followers_count], user[friends_count], user[favourites_count], user[statuses_count]

# Example:
# Status(contributors=None, truncated=False, text=u'Nintendo made a special 3DS XL for Pok\xe9mon Sun and Moon https://t.co/S28bxY9e3J', is_quote_status=False, in_reply_to_status_id=None, id=775884761390784513, favorite_count=0, _api=<tweepy.api.API object at 0x7f7d1d8ceed0>, author=User(follow_request_sent=False, has_extended_profile=False, profile_use_background_image=False, _json={u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 2673532213, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'000000', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'profile_sidebar_fill_color': u'000000', u'entities': {u'url': {u'urls': [{u'url': u'https://t.co/PO07n68QhN', u'indices': [0, 23], u'expanded_url': u'http://www.desiworldwide.in', u'display_url': u'desiworldwide.in'}]}, u'description': {u'urls': []}}, u'followers_count': 491, u'profile_sidebar_border_color': u'000000', u'id_str': u'2673532213', u'profile_background_color': u'000000', u'listed_count': 295, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 184674, u'description': u'Taking a break to write', u'friends_count': 226, u'location': u'New Delhi', u'profile_link_color': u'94D487', u'profile_image_url': u'http://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2673532213/1430202990', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'ryan_swadesi', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 94, u'name': u'Ryan Davis', u'notifications': False, u'url': u'https://t.co/PO07n68QhN', u'created_at': u'Wed Jul 23 11:27:10 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, time_zone=None, id=2673532213, _api=<tweepy.api.API object at 0x7f7d1d8ceed0>, verified=False, profile_text_color=u'000000', profile_image_url_https=u'https://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', profile_sidebar_fill_color=u'000000', is_translator=False, geo_enabled=False, entities={u'url': {u'urls': [{u'url': u'https://t.co/PO07n68QhN', u'indices': [0, 23], u'expanded_url': u'http://www.desiworldwide.in', u'display_url': u'desiworldwide.in'}]}, u'description': {u'urls': []}}, followers_count=491, protected=False, id_str=u'2673532213', default_profile_image=False, listed_count=295, lang=u'en', utc_offset=None, statuses_count=184674, description=u'Taking a break to write', friends_count=226, profile_link_color=u'94D487', profile_image_url=u'http://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', notifications=False, profile_background_image_url_https=u'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_color=u'000000', profile_banner_url=u'https://pbs.twimg.com/profile_banners/2673532213/1430202990', profile_background_image_url=u'http://abs.twimg.com/images/themes/theme1/bg.png', name=u'Ryan Davis', is_translation_enabled=False, profile_background_tile=False, favourites_count=94, screen_name=u'ryan_swadesi', url=u'https://t.co/PO07n68QhN', created_at=datetime.datetime(2014, 7, 23, 11, 27, 10), contributors_enabled=False, location=u'New Delhi', profile_sidebar_border_color=u'000000', default_profile=False, following=False), _json={u'contributors': None, u'truncated': False, u'text': u'Nintendo made a special 3DS XL for Pok\xe9mon Sun and Moon https://t.co/S28bxY9e3J', u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 775884761390784513, u'favorite_count': 0, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'https://t.co/S28bxY9e3J', u'indices': [56, 79], u'expanded_url': u'http://ift.tt/2cpX8d0', u'display_url': u'ift.tt/2cpX8d0'}]}, u'retweeted': False, u'coordinates': None, u'source': u'<a href="http://ifttt.com" rel="nofollow">IFTTT</a>', u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'775884761390784513', u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 2673532213, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'000000', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'profile_sidebar_fill_color': u'000000', u'entities': {u'url': {u'urls': [{u'url': u'https://t.co/PO07n68QhN', u'indices': [0, 23], u'expanded_url': u'http://www.desiworldwide.in', u'display_url': u'desiworldwide.in'}]}, u'description': {u'urls': []}}, u'followers_count': 491, u'profile_sidebar_border_color': u'000000', u'id_str': u'2673532213', u'profile_background_color': u'000000', u'listed_count': 295, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 184674, u'description': u'Taking a break to write', u'friends_count': 226, u'location': u'New Delhi', u'profile_link_color': u'94D487', u'profile_image_url': u'http://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2673532213/1430202990', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'ryan_swadesi', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 94, u'name': u'Ryan Davis', u'notifications': False, u'url': u'https://t.co/PO07n68QhN', u'created_at': u'Wed Jul 23 11:27:10 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'es', u'created_at': u'Wed Sep 14 02:31:57 +0000 2016', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'es', u'result_type': u'recent'}}, coordinates=None, entities={u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'https://t.co/S28bxY9e3J', u'indices': [56, 79], u'expanded_url': u'http://ift.tt/2cpX8d0', u'display_url': u'ift.tt/2cpX8d0'}]}, in_reply_to_screen_name=None, id_str=u'775884761390784513', retweet_count=0, in_reply_to_user_id=None, favorited=False, source_url=u'http://ifttt.com', user=User(follow_request_sent=False, has_extended_profile=False, profile_use_background_image=False, _json={u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 2673532213, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'000000', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'profile_sidebar_fill_color': u'000000', u'entities': {u'url': {u'urls': [{u'url': u'https://t.co/PO07n68QhN', u'indices': [0, 23], u'expanded_url': u'http://www.desiworldwide.in', u'display_url': u'desiworldwide.in'}]}, u'description': {u'urls': []}}, u'followers_count': 491, u'profile_sidebar_border_color': u'000000', u'id_str': u'2673532213', u'profile_background_color': u'000000', u'listed_count': 295, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 184674, u'description': u'Taking a break to write', u'friends_count': 226, u'location': u'New Delhi', u'profile_link_color': u'94D487', u'profile_image_url': u'http://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/2673532213/1430202990', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'ryan_swadesi', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 94, u'name': u'Ryan Davis', u'notifications': False, u'url': u'https://t.co/PO07n68QhN', u'created_at': u'Wed Jul 23 11:27:10 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, time_zone=None, id=2673532213, _api=<tweepy.api.API object at 0x7f7d1d8ceed0>, verified=False, profile_text_color=u'000000', profile_image_url_https=u'https://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', profile_sidebar_fill_color=u'000000', is_translator=False, geo_enabled=False, entities={u'url': {u'urls': [{u'url': u'https://t.co/PO07n68QhN', u'indices': [0, 23], u'expanded_url': u'http://www.desiworldwide.in', u'display_url': u'desiworldwide.in'}]}, u'description': {u'urls': []}}, followers_count=491, protected=False, id_str=u'2673532213', default_profile_image=False, listed_count=295, lang=u'en', utc_offset=None, statuses_count=184674, description=u'Taking a break to write', friends_count=226, profile_link_color=u'94D487', profile_image_url=u'http://pbs.twimg.com/profile_images/494771263676481536/6QF9LInv_normal.png', notifications=False, profile_background_image_url_https=u'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_color=u'000000', profile_banner_url=u'https://pbs.twimg.com/profile_banners/2673532213/1430202990', profile_background_image_url=u'http://abs.twimg.com/images/themes/theme1/bg.png', name=u'Ryan Davis', is_translation_enabled=False, profile_background_tile=False, favourites_count=94, screen_name=u'ryan_swadesi', url=u'https://t.co/PO07n68QhN', created_at=datetime.datetime(2014, 7, 23, 11, 27, 10), contributors_enabled=False, location=u'New Delhi', profile_sidebar_border_color=u'000000', default_profile=False, following=False), geo=None, in_reply_to_user_id_str=None, possibly_sensitive=False, lang=u'es', created_at=datetime.datetime(2016, 9, 14, 2, 31, 57), in_reply_to_status_id_str=None, place=None, source=u'IFTTT', retweeted=False, metadata={u'iso_language_code': u'es', u'result_type': u'recent'})

for tweet in tweepy.Cursor(api.search, q="Nintendo", since=(datetime.date.today() - datetime.timedelta(days=6)).strftime("%Y-%m-%d"), until=datetime.date.today().strftime("%Y-%m-%d"), count=max_amount_tweets, wait_on_rate_limit=True, since_id=last_saved_tweet).items():
    try:
        print tweet
        useful_values = {}
        values = [tweet.text, tweet.id, tweet.created_at]
        keys = ['text', 'id', 'created_at']
        for i in xrange(0, len(values)):
            if keys[i] == 'created_at':
                useful_values.update({keys[i]: values[i].strftime("%a %b %e %H:%M:%S +0000 %Y")})
            else:
                useful_values.update({keys[i]: values[i]})
        values = [tweet.author.id, tweet.author.screen_name, tweet.author.location, tweet.author.followers_count, tweet.author.friends_count, tweet.author.favourites_count, tweet.author.statuses_count, tweet.author.created_at]
        keys = ['id', 'screen_name', 'location', 'followers_count', 'friends_count', 'favourites_count', 'statuses_count', 'created_at']
        useful_values.update({'user': {}})
        for i in xrange(0, len(values)):
            if keys[i] == 'created_at':
                useful_values['user'].update({keys[i]: values[i].strftime("%a %b %e %H:%M:%S +0000 %Y")})
            else:
                useful_values['user'].update({keys[i]: values[i]})
        print useful_values
        with open(filename, 'a') as _file:
            #_file.write(tweet)
            _file.write(json.dumps(useful_values, sort_keys=True)+"\n")
            last_saved_tweet = useful_values['id']
    except tweepy.TweepError as e:
        print e

#sapi.filter(track=["Nintendo", "PlayStation", "Xbox", "Videogames"])
