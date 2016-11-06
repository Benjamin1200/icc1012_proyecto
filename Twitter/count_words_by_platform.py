import time
import sys
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import json
from datetime import datetime
from dateutil.parser import parse

# The summary is for each hour per week. (i.e. 20 times hello on week 1, 31 times bye on week 2, ...)

if __name__ == '__main__':
    time_start = time.clock()
    # Clean File.
    open("count_words_by_platform_summary.txt", 'w').close()
    files = ["project_tweets01.data", "project_tweets02.data", "project_tweets03.data", "project_tweets04.data"]
    for _file in files:
        # Write to file in append mode.
        _fo = open("count_words_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        # Code
        words = {}
        punctuation = []
        for i in xrange(0, len(string.punctuation)):
            punctuation.append(string.punctuation[i])
        stop_words = stopwords.words() + punctuation
        _data = open(_file, 'r')
        for line in _data.readlines():
            data = json.loads(line)
            date = parse(data['created_at'])
            week = date.isocalendar()[1]
            hour = date.hour
            _words = [i for i in word_tokenize(data['text'].lower()) if i not in stop_words]
            for word in _words:
                key = (week, hour, word)
                if key in words:
                    words[key] += 1
                else:
                    words[key] = 1
        for pair in words:
            print pair[0], pair[1]
        # End code
        print "\n"
    time_end = time.clock()
    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
