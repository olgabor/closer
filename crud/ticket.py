from models import db, app, Ticket
from flask import Flask, request, render_template, url_for, session, redirect, flash 
from flask_login import current_user
from datetime import datetime

def create_ticket():
    """ Function creates new ticket 
        takes the ticket values 
        checks if ticket with 'name' parameter already exists in database 
        and flashes the message back to frontend if True 
        saves new ticket in database 
        redirects to url served by 'project_show_update_delete' function 
    """
    name = request.form.get('name')
    description = request.form.get('description')
    author_id = request.form.get('author_id')
    project_id = request.form.get('project_id')
    ticket_priority = request.form.get('ticket_priority')
    ticket_status = request.form.get('ticket_status')
    time = request.form.get('due_date')
    due_date = datetime.strptime(time, '%Y-%m-%d')

    # ticket = Ticket.query.filter_by(name=name).first()  
    # if ticket:  
    #     flash('Ticket with this name address already exists')

    new_ticket = Ticket(
        name=name, 
        description=description, 
        author_id=author_id,
        project_id=project_id,
        ticket_priority=ticket_priority,
        ticket_status=ticket_status, 
        due_date=due_date)
  
    db.session.add(new_ticket)
    db.session.commit()
    return redirect(url_for('project_show_update_delete', id=project_id))

def get_all_tickets(id): 
    """ Function queries tickets by user_id 
        returns all tickets as a list of dictionaries 
    """
    all_tickets =  Ticket.query.filter((Ticket.author_id == current_user.id) and (Ticket.project_id == id))
    tickets = [ticket.ticket_as_dict() for ticket in  all_tickets]
    return  tickets 
    
def get_tickets_by_status(status):
    """ Function queries tickets by status 
        returns all tickets as a list of dictionaries 
    """
    all_tickets =  Ticket.query.filter( (Ticket.ticket_status == status) )
    tickets = [ticket.ticket_as_dict() for ticket in  all_tickets]
    return tickets  

def delete_ticket(id, pid):
    """ Function queries tickets by id 
        deletes the ticket 
        redirects to url served by 'project_show_update_delete' function 
        Raises exception if ticket by id doesn't exist in database  
    """
    ticket = Ticket.query.get(id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        return redirect(url_for('project_show_update_delete', id=pid))
    else:
        return Exception('No ticket at id {}'.format(id))

def update_ticket(id, pid, **update_values):
    """ Function updates the existing ticket
        checks if ticket exists in database
        updates ticket values and saves to database 
        redirects to url served by 'project_show_update_delete' function 
        raises exception if ticket doesn't exists 
    """
    ticket = Ticket.query.get(id)
    if ticket:
        for key, value in update_values.items():
            setattr(ticket, key, value)
        
        db.session.commit()
        return redirect(url_for('project_show_update_delete', id=pid))
    else:
        raise Exception('No Ticket at id {}'.format(id))