from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from datetime import datetime
import itertools
from datetime import datetime
from dateutil.parser import parse


class MRWordFrequencyCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, record):
        date = parse(record['created_at'])
        week = date.isocalendar()[1]
        hour = date.hour
        yield [(week, hour, record['language']), 1]

    def reducer(self, key, values):
        yield [key, sum(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]

if __name__ == '__main__':
    MRWordFrequencyCount.run()
