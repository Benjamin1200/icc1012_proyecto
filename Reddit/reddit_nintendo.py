import praw
import json
import pymongo
db = pymongo.MongoClient().carga_reddite
r = praw.Reddit(user_agent='my_cool_application')
subreddit = r.get_subreddit("Nintendo")
comments=subreddit.get_comments(limit=10000000)
for comment in comments:
	data = {}
	data['id'] = str(comment.id)
	data['user_id'] = str(comment.author)
	data['created_at'] = comment.created
	data['text'] = str(comment.body.encode('utf-8'))
	d = json.dumps(data, ensure_ascii=False)
	try:
		db.reddite.insert(json.loads(d))
	except:
		pass
