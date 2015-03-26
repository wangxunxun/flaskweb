#coding=utf-8

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from app import db,login_manager



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


#这个函数将原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


#这个函数的参数是从数据库中取回的密码散列值和用户输入的密码。返回值为True 表明密码正确
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

#generate_confirmation_token() 方法生成一个令牌，有效期默认为一小时.
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer('secrect_key', expiration)
        return s.dumps({'confirm': self.id})
#confirm() 方法检验令牌，如果检验通过，则把新添加的confirmed 属性设为True。
#除了检验令牌，confirm() 方法还检查令牌中的id 是否和存储在current_user 中的已登录
#用户匹配。如此一来，即使恶意用户知道如何生成签名令牌，也无法确认别人的账户。
    def confirm(self, token):
        s = Serializer('secrect_key')
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True





    def generate_reset_token(self, expiration=3600):
        s = Serializer('secrect_key', expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer('secrect_key')
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer('secrect_key', expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer('secrect_key')
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
