from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session 
from flask_sqlalchemy import SQLAlchemy 
import os 

#Homepage route 
@app.route('/home/')
def home():
    return render_template('home.html')

# @app.route('/projects/', methods=['GET', 'POST'])
# def show_projects():
#     all_projects = Project.query.all()
    
@app.route('/project/new', methods=['GET','POST'])
def new_project():
    return render_template('new_project.html')