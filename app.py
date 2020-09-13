from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
import os 
from crud.user import get_users, create_user
from crud.project import get_all_projects, get_project 
from models import User, db 



# user register page 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET': 
     return render_template('register.html')
    if request.method == 'POST': 
        return create_user()


#user post route 
# @app.route('/register', methods=['POST'])
# def post_register():
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')

#     #check if user exists in database 
#     user = User.query.filter_by(email=email).first()
#     print(user)

#     if user:
#         flash('Email address already exists')
#         return redirect(url_for('login'))

#     #create new user 
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
#     #add user to database 
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect(url_for('login'))


#log in 
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

#Homepage route 
@app.route('/home')
def home():
    users = get_users()
    return render_template('home.html', users=users)

@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    projects = get_all_projects()
    return projects
    # return render_template('projects.html')

#return one project 
@app.route('/projects/<int:id>')
def get_one_project(id):
    project = get_project(id)
    return project

@app.route('/project/new', methods=['GET','POST'])
def new_project():
    return render_template('new_project.html')

#ticket GET, PUT, and DELETE routes 
@app.route('/tickets/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def ticket_show_put_delete(id):
    return "SHOW, EDIT, DELETE TICKET"
