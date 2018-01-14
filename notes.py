from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

# import datetime
# post = {
# 	"author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.utcnow()
# }

# posts = db.posts
# post_id = posts.insert_one(post).inserted_id


@app.route('/')
def hello_world():
	print 'Hello Terminal'
	# x = mongo.db.users.find_one_or_404({'username': 'ally'})
	return """
    <p>Hello world</p>
    <a href="/kamran/">link text</a>
    """

@app.route('/kamran/')
def test():
	return 'kamran khan'