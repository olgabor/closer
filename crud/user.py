from models import app, db, User 
from flask import Flask, request, render_template, url_for, session, redirect, flash 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user


def create_user(): 
    """ Function creates new user 
        takes the user values 'email', 'name', 'password' 
        checks if user with 'email' parameter already exists in database 
        and flashes the message back to frontend if True 
        saves new user in database
        logs in new user with  Flask login_user 
        redirects to url served by 'all_projects' function 
    """
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('home'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit() 

    login_user(new_user)
    return redirect(url_for('all_projects'))  

def post_user():
    """ Function logs in user 
        takes the user values 'email', 'name', 'password' from request.form 
        checks if the user exists in db
        takes the user-supplied password, hashes it, and compares it to the hashed password in the database
        if user doesn't exist or password is wrong flashes the message to frontend
        and redirects to url served by 'home' function 

        if user exists logs in user with Flask login_user 
        redirects to url served by 'all_projects' function 
    """
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login credentials and try again.')
        return redirect(url_for('home')) 

    login_user(user, remember=remember)

    return redirect(url_for('all_projects'))