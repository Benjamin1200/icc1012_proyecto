from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from datetime import datetime
import itertools

class MRWordFrequencyCount(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	def mapper(self, _, record):
		date = datetime.fromtimestamp(int(record['created_at']))
		week = date.isocalendar()[1]
		yield week, int(record['created_at'])

	def reducer(self, key, values):
		for i in values:
			yield (key, datetime.fromtimestamp(i).hour), 1
	def max_reducer(self, stat, values):
		yield stat, sum(values)

	def steps(self):
		return [MRStep(mapper=self.mapper, reducer=self.reducer),
				MRStep(reducer=self.max_reducer)]

if __name__ == '__main__':
	MRWordFrequencyCount.run()
