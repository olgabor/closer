from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_required, current_user, logout_user
import os 
from crud.user import get_users, create_user, post_user
from crud.project import get_all_projects, get_project, create_project
from models import User, db



# user register page 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET': 
     return render_template('register.html')
    if request.method == 'POST': 
        return create_user()

#log in user 
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'GET': 
        return render_template('login.html')
    if request.method == 'POST': 
        return post_user()

#logout user 
@app.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('home'))

#Homepage route 
@app.route('/home')
def home():
    users = get_users()
    if current_user.is_authenticated: 
        return render_template('home.html', users=users, name=current_user.name) 
    else: 
        return render_template('home.html') 
        

@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    projects = get_all_projects()
    return projects
    

#return one project 
@app.route('/projects/<int:id>')
def get_one_project(id):
    project = get_project(id)
    return project

@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'GET':
        return render_template('new_project.html')
    if request.method == 'POST':
        return create_project()

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
