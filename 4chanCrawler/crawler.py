import basc_py4chan
import pymongo
import time

def Make_file(post):
	file = post.file
	
	name = file.filename
	original_name =file.filename_original
	file_size = file.file_size
	is_deleted = file.file_deleted
	extension = file.file_extension
	url = file.file_url
	thumbnail_fname = file.thumbnail_fname
	thumbnail_url = file.thumbnail_url

	file_data = {
		'name':name,
		'original_name':original_name,
		'size':file_size,
		'extension':extension,
		'url':url,
		'thumbnail_url':thumbnail_url,
		'thumbnail_fname':thumbnail_fname
	}

	return file_data
	
def Make_post(post):

	post_id = post.post_id
	poster_id = post.poster_id
	poster_name = post.name
	poster_email = post.email
	subject = post.subject
	comment = post.text_comment
	timestamp = post.timestamp
	url = post.url
	datetime = post.datetime
	post_file = {}
	has_file = post.has_file
	if has_file:
		post_file = Make_file(post)

	post_data = {
		'id':post_id,
		'poster_name':poster_name,
		'poster_id':poster_id,
		'poster_email':poster_email,
		'subject':subject,
		'comment':comment,
		'timestamp':timestamp,
		'url':url,
		'datatime':datetime,
		'file':post_file
	}

	return post_data
	
#THREAD
def Make_thread(thread_id, board):
	thread = board.get_thread(thread_id)
	board_name = board.name
	is_closed = thread.closed
	thread_url = thread.url
	topic = thread.topic
	
	topic_data = Make_post(topic)

	posts = thread.all_posts
	all_post_data = []
	for post in posts:
		post_data = Make_post(post)
		all_post_data.append(post_data)

	
	thread_data = {
		'id':thread_id,
		'is_closed':is_closed,
		'url':thread.url,
		'topic':topic_data,
		'board':board_name,
		'posts':all_post_data
	}

	return thread_data

def Crawler_board():
	db = pymongo.MongoClient().fourchanVideoGamess	
	all_boards_names = ['v','vg','vr']
	for board_name in all_boards_names:
		board = basc_py4chan.Board(board_name)
		all_threads_ids = board.get_all_thread_ids()
		print "tiene los ids"
		for thread_id in all_threads_ids:
			db.VideoGamess.delete_many({u'id':thread_id})
			print "en el for"
			new_thread = Make_thread(thread_id, board)
			result = db.VideoGamess.insert_one(new_thread)

'''	
def test_db():
	db2 = pymongo.MongoClient().test_vg
#	data = db2.test_vgg.find({u'id':12345})
	db2.test_vgg.delete_many({u'id':123})
	data_s = {
		'id':123,
		'url':"www.hola.com",
		'dll':"segu"
	}
	db2.test_vgg.insert_one(data_s)

'''	

#board = basc_py4chan.Board('v')
#thread_ids = board.get_all_thread_ids()

Crawler_board()
#test_db()
#Select_some_data(352912725)


'''	
	

		
user_time = int(raw_input('ingrese el tiempo '))
itera = int(raw_input('numero de iteraciones '))
count = 0	
while count < itera:
	print "iteracion numero : "+str(count)
	Crawler_board()
	count += 1
	time.sleep(user_time)
'''	















