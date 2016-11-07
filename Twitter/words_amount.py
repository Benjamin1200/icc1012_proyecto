from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import time
import itertools
import sys
from datetime import datetime
from dateutil.parser import parse
import operator

class MRWordFrequencyCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, record):
        hour = record['hour']
        week = record['week']
        word = record['word']
        yield [(week, hour, word), 1]

    def reducer(self, key, values):
        yield [(key[0], key[1]), (sum(values), key[2])]

    def reducer2(self, key, values):
        counts = []
        words = []
        for value in values:
            words.append(value[1])
            counts.append(value[0])
        pair_word_count = {}
        for i in xrange(0, len(words)):
            pair_word_count[words[i]] = counts[i]
        top_words = sorted(pair_word_count.items(), key=lambda x: (x[1], operator.itemgetter(0)), reverse=True)
        for word in top_words[0:20]:
            #print user[0], user[1]
            yield [(key[0], key[1], word[0]), word[1]]

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer), MRStep(reducer=self.reducer2)]


if __name__ == '__main__':
    #time_start = time.clock()
    MRWordFrequencyCount().run()
    #time_end = time.clock()
    #print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
