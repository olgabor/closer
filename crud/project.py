from models import app, Project 
from flask import jsonify 

def get_all_projects():
    all_projects = Project.query.all()
    results = [project.project_as_dict() for project in all_projects] 
    return jsonify(results)



def get_project(id):
    user = Project.query.get(id)
    if project:
      return jsonify(project.as_dict())
    else:
      raise Exception('Error getting project at {}'.format(id))