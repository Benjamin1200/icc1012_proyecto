import language_detect as ld
import sentiment_analyzer as sa
import json

# The preclassified files only have 100 registers, because we did not have more time to pre-classificate
language_file = "preclassified_language.data"
sentiment_file = "preclassified_sentiment.data"

_output = ld.set_language_for_each_tweet(language_file)
classifier = sa.init_classifier()
_output2 = sa.classify_file(sentiment_file, classifier)

# Check correct predictions of: languages
count_errors = 0
count_tweets = 0
with open(_output, 'r') as fo:
    for line in fo.readlines():
        if len(line) != 0:
            values = json.loads(line)
            if values['language'] != values['real_language']:
                count_errors += 1
            count_tweets += 1
print "The percentage of correct predictions for languages is: {}%".format(float(count_tweets - count_errors) / count_tweets * 100)

# Check correct predictions of: sentiment
count_errors = 0
count_tweets = 0
with open(_output2, 'r') as fo:
    for line in fo.readlines():
        if len(line) != 0:
            values = json.loads(line)
            if values['classification'] != values['real_classification']:
                count_errors += 1
            count_tweets += 1
print "The percentage of correct predictions for sentiments is: {}%".format(float(count_tweets - count_errors) / count_tweets * 100)