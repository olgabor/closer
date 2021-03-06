from models import app, User, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_required, current_user, logout_user
from crud.user import create_user, post_user
from crud.project import get_all_projects, get_project, create_project, update_project
from crud.ticket import create_ticket, get_all_tickets, delete_ticket, get_tickets_by_status, update_ticket
from models import User, db, Project, Ticket


#homepage route 
@app.route('/', methods=['GET','POST'])
def home():
     return render_template('home.html')


#user register page 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST': 
        return create_user()


#login user 
@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST': 
        return post_user()


#logout user 
@app.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('home'))


#renders 'projects' page and manages creating new project         
@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'GET':
        return render_template('new_project.html')
    if request.method == 'POST':
        return create_project()


@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    projects = get_all_projects()
    tickets =  get_all_tickets(id)
    return render_template('projects.html', projects=projects, tickets=tickets) 


@app.route('/projects/<int:id>', methods=['GET', 'PUT'])
def project_show_update_delete(id):
    if request.method == 'GET':
        project = get_project(id)
        tickets =  get_all_tickets(id)
        toDo_tickets = get_tickets_by_status('ToDo')
        inProgress_tickets = get_tickets_by_status('InProgress')
        complete_tickets = get_tickets_by_status('Done')
        print('line 67 tickets length', (len(tickets)))
        print('line 68 tickets length', (len(complete_tickets)))
        return render_template('show_project.html', 
                                project=project, 
                                tickets=tickets, 
                                toDo_tickets=toDo_tickets, 
                                inProgress_tickets=inProgress_tickets,
                                complete_tickets=complete_tickets, 
                                number_tickets=len(tickets),
                                number_complete_tickets=len(complete_tickets) ) 
    if request.method == 'PUT':

        project = Project.query.get(id)
        if project:
            project.title = request.form.get('title')
            project.description = request.form.get('description')
            db.session.commit()

    return redirect(url_for('all_projects'))


#creates new ticket 
@app.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'GET':
        return render_template('new_ticket.html')
    if request.method == 'POST':
        return create_ticket()


#ticket GET, PUT and DELETE routes 
@app.route('/projects/<int:pid>/tickets/<int:id>', methods=['GET', 'PUT', 'POST'])
def ticket_show_put_delete(id, pid):
    print('Line 92', request.method, id , pid)
    if request.method == 'GET':
        return delete_ticket(id, pid)
    if request.method == 'POST':
        return update_ticket(id, pid, **request.form)
    else:
        return "SHOW, EDIT, DELETE TICKET"


@app.errorhandler(Exception)
def unhandled_exception(e):
  app.logger.error('Unhandled Exception: %s', (e))
  message_str = e.__str__()
  return jsonify(message=message_str.split(':'))
