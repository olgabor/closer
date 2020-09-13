from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum 
from enum import Enum
from sqlalchemy import Integer, Enum

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/closer'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

#Users model 
class User(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100)) 
    password = db.Column(db.String(100))
    project = db.relationship("Project", backref="users", cascade="all, delete")

    def __repr__(self):
            return f'User(id={self.id}, email="{self.email}", name="{self.name}")'
    
    # def user_as_dict(self):
    #     return [{
    #         id: self.id,
    #         email: self.email,
    #         name: self.name
    #         }]

    def user_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class Project(db.Model): 
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(250)) 
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    
    #realtionship to Ticket 
    ticket = db.relationship("Ticket", backref="project", cascade="all, delete")


    def __repr__(self):
            return f'Project(id={self.id}, title="{self.title}", description="{self.description}" , author_id="{self.author_id}")'

    def project_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

class Ticket_Status(enum.Enum):
    ToDo = 'To Do'
    InProgress = 'In Progress'
    Done = 'Done'
    Cancelded = 'Cancelded'

class Ticket_Priority(enum.Enum):
    Higher = 'Higher'
    High = 'High'
    Medium = 'Medium'
    Low = 'Low'

class Ticket(db.Model): 
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.Text) 
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='SET NULL')) #if project gets deleted this field gets deleted 
    image = db.Column(db.String(300))
    ticket_status = db.Column(db.Enum(Ticket_Status), default=Ticket_Status.ToDo, nullable=False)
    ticket_priority = db.Column(db.Enum(Ticket_Priority), default=Ticket_Priority.Medium,  nullable=False)
    due_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 

    def __repr__(self):
            return f'Ticket(id={self.id}, summary="{self.summary}", created_on="{self.created_on}" , author_id="{self.author_id}",  project_id ="{self.project_id}", status="{self.status}", priority="{self.priority}")'

  

