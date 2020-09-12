from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session 
from flask_sqlalchemy import SQLAlchemy 
import os 

# user register 
@app.route('/register/', methods=['GET','POST'])
def register():
    return render_template('register.html')

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

