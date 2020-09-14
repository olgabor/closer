from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy 
import os 
from crud.user import get_users, create_user, post_user
from crud.project import get_all_projects, get_project 
from models import User, db
from flask_login import login_required, current_user


# user register page 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET': 
     return render_template('register.html')
    if request.method == 'POST': 
        return create_user()

#log in 
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'GET': 
        return render_template('login.html')
    if request.method == 'POST': 
        return post_user()

#Homepage route 
@app.route('/home')
@login_required
def home():
    users = get_users()
    return render_template('home.html', users=users, name=current_user.name)

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



#WTF forms 
# class RegistrationForm(Form):
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
