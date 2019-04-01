from flask import Flask
from flask_msearch import Search
from config import Config
import os

search = Search()
search.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

db = SQLAlchemy(app)

class Course(db.Model):
    __tablename__ = 'course'
    __searchable__ = ['id', 'name', 'description']

	#which columns can be searched:
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(30))
    description = db.Column(db.String(100))

@app.route("/search")
def w_search():
    keyword = request.args.get('keyword')
    results = Post.query.msearch(keyword,fields=['title'],limit=20).filter(...)
    return 'return'

@app.route("/return", methods = ['post'])
def return():
    return render_template('result.html')
