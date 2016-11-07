import pymongo
import time


db = pymongo.MongoClient().carga_twitter
count = 100
suma1 = 0
suma2 = 0
suma3 = 0
while count > 0:
	tic = time.clock()
	pipe = [{ '$group': { '_id': '$place.country', 'count': { '$sum': 1 } } },  { '$sort': { '_id': 1 }} ]
	db.tweet.aggregate(pipeline=pipe)
	toc = time.clock()
	suma1 += toc -tic 
	tic = time.clock()
	pipe =[{ '$group': { '_id': { 'hour': {'$hour': '$timestamp_ms'}, }, 'count': {'$sum': 1} } },  { '$sort': { 'hour': 1 } }]
	db.tweet.aggregate(pipeline=pipe)
	toc = time.clock()
	suma2 += toc - tic 
	tic = time.clock()
	db.tweet.find({ 'text': '/^RT @/' }).count()
	toc = time.clock()
	suma3 += toc - tic 
	print count
	count -=1
	
print "Tiempo", suma1 / 100
print "Tiempo", suma2 / 100
print "Tiempo", suma3 / 100
