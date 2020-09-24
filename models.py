from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum 
from enum import Enum
from sqlalchemy import Integer, Enum
from flask_login import UserMixin, LoginManager, AnonymousUserMixin
import psycopg2, os 
from sqlalchemy import create_engine



app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///closer'
app.config['DEBUG'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

DATABASE_URL = 'postgresql:///closer' 

# DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
engine = create_engine('postgresql:///closer'')

# Sets the secret key to random bytes
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

def connect_db(app):
    # Connect to database
    db.app = app
    db.init_app(app)

connect_db(app)
db.create_all()

#Users model 
class User(UserMixin, db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100)) 
    password = db.Column(db.String(100))
    project = db.relationship("Project", backref="users", cascade="all, delete") #sets realtionship to Project table 

    def __repr__(self):
            return f'User(id={self.id}, email="{self.email}", name="{self.name}")'
 
    def user_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class Project(db.Model): 
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(250)) 
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    ticket = db.relationship("Ticket", backref="project", cascade="all, delete") #sets realtionship to Ticket table 


    def __repr__(self):
            return f'Project(id={self.id}, title="{self.title}", description="{self.description}" , author_id="{self.author_id}")'

    def project_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    
class Ticket_Priority(enum.Enum):
    Higher = 1
    High = 2
    Medium = 3
    Low = 4

class Ticket_Status(enum.Enum):
    ToDo = 1
    InProgress = 2
    Done = 3

class Ticket(db.Model): 
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) 
    description = db.Column(db.Text) 
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='SET NULL')) #if project gets deleted this field gets deleted 
    image = db.Column(db.String(500))
    ticket_priority = db.Column(db.Enum(Ticket_Priority), default=Ticket_Priority.Medium,  nullable=True )
    ticket_status = db.Column(db.Enum(Ticket_Status), default=Ticket_Status.ToDo, nullable=True )
    due_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True ) 

    def __repr__(self):
            return f'Ticket(id={self.id}, name="{self.name}", description="{self.description}",  date_posted="{self.date_posted}" , author_id="{self.author_id}",  project_id ="{self.project_id}", due_date="{self.due_date}")'

    def ticket_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  

#user loaded function 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)