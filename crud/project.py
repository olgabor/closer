from models import db, app, Project
from flask import Flask, request, render_template, url_for, session, redirect, flash 
from flask_login import current_user

def get_project(id):
    """ Function takes the id parameter 
        queries project by id in database 
        returns the project 
        raises exception if projects doesn't exists 
    """ 
    project = Project.query.get(id)
    if project:
      return project
    else:
        raise Exception('Error getting project at {}'.format(id))

def create_project(): 
    """ Function creates new project 
        takes the project parameters 'title', 'description', 'author_id' 
        checks if project with 'title' parameter already exists in database 
        and flashes the message back to frontend if True 
        Saves new project in database 
        redirects to url served by 'all_projects' function 
    """
    title = request.form.get('title')
    description = request.form.get('description')
    author_id = request.form.get('author_id')

    project = Project.query.filter_by(title=title).first()
    
    if project:
        flash('Project address already exists')

    new_project = Project(title=title, description=description, author_id=author_id)
    db.session.add(new_project)
    db.session.commit()
    return redirect(url_for('all_projects'))

def get_all_projects():
    """ Function queries all projects by user_id 
        returns all projects as a list of dictionaries 
    """
    all_projects =  Project.query.filter(Project.author_id == current_user.id)
    results = [project.project_as_dict() for project in all_projects] 
    return all_projects

def update_project(id, title, description):
    """ Function updates the existing project
        checks if project exists in database
        updates title and description and saves to database 
        raises exception if projects doesn't exists 
    """
    project = Project.query.get(id=id)

    if project:
        project.title = title
        project.description = description
        
        db.session.commit()
        return redirect(url_for('all_projects'))

    else:
        raise Exception('No Project at id {}'.format(id))