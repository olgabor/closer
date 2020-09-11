from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/closer'


db = SQLAlchemy(app)


class User(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Intger, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100)) 
    password = db.Column(db.String(100))

    
    def __repr__(self):
            return f'User(id={self.id}, email="{self.email}", name="{self.name}")'