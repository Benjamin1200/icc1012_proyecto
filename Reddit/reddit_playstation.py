# -*- coding: utf-8 -*-
import praw
import json
r = praw.Reddit(user_agent='my_cool_application')
subreddit = r.get_subreddit("Playstation")

with open('playstation_reddite.txt', 'a') as outfile:
	subreddit = r.get_subreddit("Playstation")
	comments=subreddit.get_comments(limit=1000000)
	for comment in comments:
		data = {}
		data['id'] = str(comment.id)
		data['user_id'] = str(comment.author)
		data['created_at'] = comment.created
		data['text'] = str(comment.body.encode('utf-8'))
		json.dump(data, outfile, separators=(',', ':'), ensure_ascii=False, encoding="utf-8")
		outfile.write('\n')
outfile.close()
