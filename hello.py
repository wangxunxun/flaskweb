#coding=utf-8
'''
Created on 2015年3月13日

@author: wangxun
'''
from flask import Flask,render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/user/<id>')
def get_user(id):
    user = 'load_user(id)'
    if not user:
        abort(404)
    return '<h1>hello,%s</h1>'%id

if __name__=="__main__":
    app.run(debug=True)