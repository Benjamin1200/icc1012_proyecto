from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import time
import itertools
import sys

class MRWordFrequencyCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, record):
        yield [record['user_id'], 1]

    def reducer(self, key, values):
        yield [key, 1]

    def mapper2(self, key, values):
        yield ['amount_users', values]

    def reducer2(self, key, values):
        yield [key, sum(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer),
                MRStep(mapper=self.mapper2, reducer=self.reducer2)]


if __name__ == '__main__':
    #time_start = time.clock()
    MRWordFrequencyCount().run()
    #time_end = time.clock()
    #print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
