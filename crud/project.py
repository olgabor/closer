from models import db, app, Project, Ticket 
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from flask_login import current_user

def get_project(id):
    project = Project.query.get(id)
    if project:
      return jsonify(project.project_as_dict())
    else:
        raise Exception('Error getting project at {}'.format(id))


def create_project(): 
    title = request.form.get('title')
    description = request.form.get('description')
    author_id = request.form.get('author_id')

    #check if user exists in database 
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
    # return jsonify(results)
    return all_projects

# def update_project(id, **update_values):
#   project = Project.query.get(id)

#   print("PROJECT", project)
#   if project:
#     for key, value in update_values.items():
#       setattr(project, key, value)
#     db.session.commit()
#     print("PROJECT " , project  )
#     return jsonify(project.project_as_dict())
#   else:
#     raise Exception('No Project at id {}'.format(id))

def update_project(id, title, description):
    print(id, title, description)

    project = Project.query.get(id=id)
    print(project.id, project.title )
    if project:
        project.title = title
        project.description = description
        
        db.session.commit()
        return redirect(url_for('all_projects'))

    else:
        raise Exception('No Project at id {}'.format(id))