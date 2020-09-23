from models import db, app, Project, Ticket 
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from flask_login import current_user

def get_project(id):
    project = Project.query.get(id)
    if project:
      return project
    else:
        raise Exception('Error getting project at {}'.format(id))

def create_project(): 
    title = request.form.get('title')
    description = request.form.get('description')
    author_id = request.form.get('author_id')

    #checks if project exists in database 
    project = Project.query.filter_by(title=title).first()
    
    if project:
        flash('Project address already exists')
        
    #create new project
    new_project = Project(title=title, description=description, author_id=author_id)
    db.session.add(new_project)
    db.session.commit()
    return redirect(url_for('all_projects'))

def get_all_projects():
    all_projects =  Project.query.filter(Project.author_id == current_user.id)
    results = [project.project_as_dict() for project in all_projects] 
    return all_projects

def update_project(id, title, description):
    project = Project.query.get(id=id)

    #checks if project exists in database 
    if project:
        project.title = title
        project.description = description
        
        db.session.commit()
        return redirect(url_for('all_projects'))

    else:
        raise Exception('No Project at id {}'.format(id))