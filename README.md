
## Closer

### Introduction
Manage your projects and tasks with a Closer productivity app. 

Sign up for an account with Closer: <https://closer-sei.herokuapp.com/>

#### Built with    
* Flask 
* PostgreSQL 
* SQLAlchemy
* Bootstrap 
* HTML
* jQuery 

### Features 
- Create your own account
- Create non limited amount of projects 
- Have the individual tickets to your project 
- Apply status and priority labels to each individual ticket 
- Control your project productivity with updating and deleting ticket statuses and due dates 

## Run  
```
$ export FLASK_APP=js_example
$ flask ru 
Open http://127.0.0.1:5000 in a browser. 
```
## Install 
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -e .
```
## Run Unit Tests 
```
python -m unittest
```

### Entity Relationship Diagram 
![ER_models_diagram](/images/ER_models_diagram.png?raw=true "ER_models_diagram") 

 Homepage 
![Homepage](/images/Closer_Homepage.png?raw=true "Homepage") 

 Project Landing page
![project_Landing_page](images/Closer_project_landing_page.png?raw=true "project_Landing_page")  

 Create new project
![create_new_project](/images/Closer_add_new_project.png?raw=true "create_new_project") 

 Project dashboard
![Closer_project_dashboard](/images/Closer_project_dashboard.png?raw=true "Closer_project_dashboard") 

 Create new ticket 
![Closer_add_new_ticket](/images/Closer_add_new_ticket.png?raw=true "Closer_add_new_ticket") 

## Planned Features

1. Utilize Google calendar API to add events to user calendar 
2. Add flash messages when new user, project, ticket were created 
3. Fix current date not saving as default
