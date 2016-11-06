from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import time
import itertools
import operator
import sys

class MRWordFrequencyCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, record):
        name = record['user_id']
        if name == "GoGoGadgetReddit" or name == "[deleted]" or name == " ":
            pass
        else:
            yield [record['user_id'], 1]

    def reducer(self, key, values):
        yield ["top_user", (sum(values), key)]

    def reducer2(self, key, values):
        user_ids = []
        user_tweets = []
        for value in values:
            user_ids.append(value[1])
            user_tweets.append(value[0])
        user = {}
        for i in xrange(0, len(user_ids)):
            user[user_ids[i]] = user_tweets[i]
        top_users = sorted(user.items(), key=lambda x: (x[1], operator.itemgetter(0)), reverse=True)
        for user in top_users[0:10]:
            #print user[0], user[1]
            yield [user[0], user[1]]

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer),
                MRStep(reducer=self.reducer2)]


if __name__ == '__main__':
    #time_start = time.clock()
    MRWordFrequencyCount().run()
    #time_end = time.clock()
    #print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
