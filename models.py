from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import enum 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/closer'


db = SQLAlchemy(app)


class User(db.Model): 
    __tablename__ = 'user'

    id = db.Column(db.Intger, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100)) 
    password = db.Column(db.String(100))
    #realtionship with Project table 
    # project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = relationship("Project", backref="user", cascade="all, delete")

    def __repr__(self):
            return f'User(id={self.id}, email="{self.email}", name="{self.name}" , projects="{self.project_id}")'

    
class Project(db.Model): 
    __tablename__ = 'project'

    id = db.Column(db.Intger, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(250)) 
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    
    #realtionship to Ticket 
    tickets = relationship("Ticket", backref="project", cascade="all, delete")


    def __repr__(self):
            return f'Project(id={self.id}, title="{self.title}", description="{self.description}" , author_id="{self.author_id}")'


class Status(enum.Enum):
    'To Do' = 1
    'In Progress' = 2
    'Done'  = 3
    'Cancelded' = 4 

class Priority(enum.Enum):
    'Higher' = 1
    'High' = 2
    'Medium'  = 3
    'Low' = 4 

class Ticket(db.Model): 
    __tablename__ = 'ticket'

    id = db.Column(db.Intger, primary_key=True)
    summary = db.Column(db.Text) 
    created_on = db.Column(db.Time, TIEMESTAMP, default=now, timezone=True) 
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='SET NULL')) #if project gets deleted this field gets deleted 
    image = db.Column(db.String(300))
    status = db.Enum(Status)
    priority = db.Enum(Priority)
    due_date = db.Column(db.Time, TIEMESTAMP, timezone=True) 

    def __repr__(self):
            return f'Ticket(id={self.id}, summary="{self.summary}", created_on="{self.created_on}" , author_id="{self.author_id}",  project_id ="{self.project_id}", status="{self.status}", priority="{self.priority}")'

  

