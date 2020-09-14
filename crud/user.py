from models import app, db, User 
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user


# return all users from database
def get_users():
    all_users = User.query.all()
    results = [user.user_as_dict() for user in all_users] 
    return jsonify(results)

def create_user(): 
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #check if user exists in database 
    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('home'))

    #create new user 
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    #add user to database 
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))


def post_user():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('register')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('all_projects'))