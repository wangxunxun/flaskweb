#coding=utf-8
'''
Created on 2015年3月19日

@author: xun
'''
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:test@69.164.202.55/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'beyondsoftbugzilla@163.com'
app.config['MAIL_PASSWORD'] = 'wangxun2'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db =SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)

login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


from app import views
