from flask import Flask
from flask import escape
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    lst = os.listdir('posts/')
    lst.sort(key=lambda x: int(x[:len(x) - 4]), reverse=True)
    list_text = []
    for text_file in lst:
        fin = open('posts/' + text_file, "r")
        list_text.append(fin.read())
    return render_template('posts.html', posts_list=list_text)


@app.route('/posts/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/save', methods=['POST'])
def save():
    text = format(request.form['text'])
    list_dir = os.listdir('posts/')
    file_name = str(len(list_dir) + 1)
    text_file = open('posts/' + file_name + '.txt', 'w')
    text_file.write(text)
    text_file.close()
    return redirect(url_for('posts'))


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
