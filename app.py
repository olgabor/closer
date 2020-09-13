from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from flask_sqlalchemy import SQLAlchemy 
import os 
from crud.user import get_users, create_user, login_user
from crud.project import get_all_projects, get_project 
from models import User, db 


# user register page 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET': 
     return render_template('register.html')
    if request.method == 'POST': 
        return create_user()

#log in 
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    return login_user()

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
