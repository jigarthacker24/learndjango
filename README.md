# Learn Django

## Installing Django
`python -m pip install -e django`

`python -m django --version`

### Starting new project and starting app in the project
You can create project at any location.

> Creating/starting project
`django-admin startproject projectname`
This will create a new project folder named *projectname*.
Project folder should contain *manage.py*.

> Creating/starting app 
`python manage.py startapp appname`

> Apply model changes.
`python manage.py startmigrating appname`

`python manage.py migrate`

> Start app server
`python manage.py runserver`
This will start app server at localhost:8000 port. *Recommended!*
**OR**
`python manage.py runserver 8080`
This will start app server at localhost:8080 port.
**OR**
`python manage.py runserver ip:8080`
This will start app server at ip:8080 port.


