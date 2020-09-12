from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session 
from flask_sqlalchemy import SQLAlchemy 
import os 

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
    return render_template('home.html')

@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    # projects = Project.query.all()
    return render_template('projects.html')
    
@app.route('/project/new', methods=['GET','POST'])
def new_project():
    return render_template('new_project.html')

#ticket GET, PUT, and DELETE routes 
@app.route('/tickets/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def ticket_show_put_delete(id):
    return "SHOW, EDIT, DELETE TICKET"
   
