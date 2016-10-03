import praw
import json
r = praw.Reddit(user_agent='my_cool_application')
subreddit = r.get_subreddit("Videogames")
comments=subreddit.get_comments(limit=10000000)
with open('videogames_reddite.txt', 'a') as outfile:
	for comment in comments:
		data = {}
		data['id'] = str(comment.id)
		data['user_id'] = str(comment.author)
		data['created_at'] = comment.created
		data['text'] = str(comment.body.encode('utf-8'))
		json.dump(data, outfile, separators=(',', ':'), ensure_ascii=False)
		outfile.write('\n')
outfile.close()