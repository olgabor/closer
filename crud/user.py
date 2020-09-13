from models import app, User 
from flask import jsonify 

# return all users from database as a json object 
def get_users():
    all_users = User.query.all()
    results = [user.user_as_dict() for user in all_users] 
    return jsonify(results)