**Django Task Manager API**

This is a simple RESTful Task Management System built with Django and Django REST Framework (DRF). It supports full CRUD operations for managing TODO tasks with `title`, `description`, and `date`.

Features

-  Create a task  
-  View all tasks  
-  Search tasks by title or date  
-  Sort tasks by date  
-  Edit (Update) a task  
-  Delete a task

Folders

-  task_manager/
├── task_manager/ # Main project settings
├── task_manager_app/ # App with models, views, serializers, and urls
├── tests.py # Unit and integration tests
└── manage.py

**Apply migrations**

python manage.py makemigration
python manage.py migrate

**Final step**

python manage.py runserver
python manage.py test  -- to run test cases

API Endpoints:

GET :	/tasks/	List all tasks

GET :	/tasks/?search=abc	Search tasks by title

GET	: /tasks/?search_date=yyyy-mm-dd	Search tasks by date

GET	: /tasks/?sort_by_date=true	Sort tasks by date

POST :	/tasks/	Create a new task

PATCH	: /tasks/<id>/	Update a task by ID

DELETE : /tasks/<id>/	Delete a task by ID

**THANK YOU**
