import unittest 
from app import app, db 
from models import User, Project, Ticket, Ticket_Priority 
from datetime import datetime

class TestApp(unittest.TestCase):
    
    #executed prior to each test 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/closer_test' 
        self.app = app.test_client()
        db.create_all()
    
    #executed after each test 
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    #index route returns 200 
    def test_index(self):
        test = app.test_client(self)
        response = test.get('/')
        self.assertAlmostEqual(response.status_code, 200)
 
    #user saves to database 
    def test_user(self):
        user = User(email='unittest@sample.com', name='unittestUser', password='password')
        db.session.add(user)
        db.session.commit()
        test = User.query.filter_by(email='unittest@sample.com').first() 
        assert test.email == 'unittest@sample.com'
        assert test.name == 'unittestUser'
        assert test.password == 'password'

    #project saves to database 
    def test_project(self):
        project = Project(title='Test_project', description='unittest !@#$%^&*()1234')
        db.session.add(project)
        db.session.commit()
        test = Project.query.filter_by(title='Test_project').first() 

        assert test.title == 'Test_project'
        assert test.description == 'unittest !@#$%^&*()1234'
        
    #ticket saves to database 
    def test_project(self):
        ticket = Ticket(name = 'Test_ticket', 
                        description = 'unittest ticket !@#$%^&*()1234',
                        ticket_priority = 'Medium', 
                        ticket_status = 'ToDo'
                        )
        db.session.add(ticket)
        db.session.commit()
        test = Ticket.query.filter_by(name='Test_ticket').first() 

        assert ticket.name == 'Test_ticket'
        assert ticket.description == 'unittest ticket !@#$%^&*()1234'
        
  

if __name__ == "__main__":
    unittest.main()
