from models import app, db, User 
from flask import Flask, request, jsonify, render_template, url_for, session, redirect, flash 
from werkzeug.security import generate_password_hash, check_password_hash


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