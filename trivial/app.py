from flask import Flask
from flask_msearch import Search
from config import Config
import os

search = Search()
search.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

class Post(db.Model):
    __tablename__ = 'post'
    __searchable__ = ['title', 'content', 'tag']

    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    tag = db.Column(db.Integer, primary_key=True)

@app.route("/search")
def w_search():
    keyword = request.args.get('keyword')
    results = Post.query.msearch(keyword,fields=['title'],limit=20).filter(...)
    return ''

@app.route("/return", methods = ['post'])
def return():
    return render_template('result.html')
