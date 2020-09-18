from models import db, app, Project, Ticket
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from flask_login import current_user
from datetime import datetime

def create_ticket():

    #get values from form fields 
    name = request.form.get('name')
    description = request.form.get('description')
    author_id = request.form.get('author_id')
    project_id = request.form.get('project_id')
    ticket_priority = request.form.get('ticket_priority')
    ticket_status = request.form.get('ticket_status')
    time = request.form.get('due_date')
    due_date = datetime.strptime(time, '%Y-%m-%d')
    # date_posted = request.form.get('date_posted')


    # ticket = Ticket.query.filter_by(name=name).first() 

    #if ticket exists flash the message 
    # if ticket:  
    #     flash('Ticket with this name address already exists')

    new_ticket = Ticket(
        name=name, 
        description=description, 
        author_id=author_id,
        project_id=project_id,
        ticket_priority=ticket_priority,
        ticket_status=ticket_status, 
        # date_posted=date_posted,
        due_date=due_date
        )
  
    db.session.add(new_ticket)
    db.session.commit()
    t = new_ticket 
    # return redirect(url_for('all_projects'))
    return redirect(url_for('all_projects'))

# def get_project(id):
#     project = Project.query.get(id)
#     if project:
#       return jsonify(project.project_as_dict())
#     else:
#         raise Exception('Error getting project at {}'.format(id))

def get_all_tickets(id): 

    # all_tickets =  Ticket.query.filter( Ticket.author_id == current_user.id))
    # results = [ticket.ticket_as_dict() for ticket in all_tickets] 
    all_tickets =  Ticket.query.filter((Ticket.author_id == current_user.id) and (Ticket.project_id == id))
    tickets = [ticket.ticket_as_dict() for ticket in  all_tickets]
    return  tickets 
    

def get_tickets_by_status(status):
    all_tickets =  Ticket.query.filter( (Ticket.ticket_status == status) )
    tickets = [ticket.ticket_as_dict() for ticket in  all_tickets]
    # (Ticket.author_id == current_user.id) and (Ticket.project_id == id) and
    print('LINE 63 get_ToDo_tickets(id)!!!!!!!!!!!!!!!!!!!!!!' , tickets)
    # Todo_tickets = Ticket.query.filter((Ticket.ticket_status == 'ToDo'))
    return tickets  


def delete_ticket(id, pid):

    ticket = Ticket.query.get(id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        
        return redirect(url_for('project_show_update_delete', id=pid))
    else:
        return Exception('No ticket at id {}'.format(id))

    