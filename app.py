from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session 
from flask_sqlalchemy import SQLAlchemy 
import os 
from crud.user import get_users
from crud.project import get_all_projects, get_project 

# user register 
@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

#log in 
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

#Homepage route 
@app.route('/home')
def home():
    users = get_users()
    return users
    # return render_template('home.html', users=users)

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
   
