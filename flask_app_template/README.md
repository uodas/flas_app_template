# Overview

This is a general template of an app that is used to create tools by ...
The template is fully functional, it has some mockup
functionality and can be run (mostly) right away as is. 

The idea is to use this template when writing your own app. This way your app
will have overall similar structure and will be easier to understand to other
developers. Also, you can focus on the logic specific to your application and 
don't worry about general functionality as it is mainly covered by this template.

## What is demonstrated in this template (what recipes)

- using argparse
- using logging
- using unittest
- basic Flask app
- jinja2 templates
- SQLAlchhemy in Flask app
- Bootstrap 4 in Flask app
- APScheduler in Flask app
- forms with flask_wtf
- dockerfile
- docker-compose file
- using SQLite in Flask app
- download a file from Flask app
  
## General guidlines

- Try to maintain separation between components of an app. E.g. backend vs 
  frontend, separate file for config, separate folder for various functions, etc.
- Do implement logging
- Do implement argparse
- Make sure your backend scripts can be run as part of the app as well as 
  separately on the command line.
- Create unit tests for main functions
- Keep as much configuration as posible in `config.yaml` in the root folder
- Generally, our CurrentWorkingDirectory is the root of the project `vilma_app_templates`
so start your main app scripts from the CWD, e.g. (`start main_frontend.py` from 
  flask_app_templates folder and not from the frontend folder)

## Technologies and main Python modules

- Python - we use Python 3.X.Y
	- argparse - use the module to parse command line arguments 
	- logging - module to use for logs
- SQLalchmey - we suggest to use this module for work with SQL databases
- Flask - web application framework
	- flask_sqlalchemy - SQLalchmey in Flask app
	- flask_bootstrap - (optional) use for easier styling of HTML
	- flask_wtf - use to create web forms if needed
	- Jinja2 - templating language, in simple workds we use it for HTML pages from 
our Flask app
- Docker - we use docker to containerize and deploy the app

# General project structure
## Directories structure

- **backend** - typicaly here we put the code with the main logic. This is usually 
the code that does the main job and that can be also easily run on the command
line.
	- `main_backend.py` - the main backend script, the entry point. Create other 
	files and folders here as needed. The script has the main function 
	(`main_back_foo`) that starts the tool, but also it can be run from command line.
	- `additional_backend.py` - just an example of additional script. It has a foo
	to read args, setup logger, read in `config.yaml`, etc. 
- **frontend** - Flask app stuff
	- **webapp** - main Flask app files
		- static - static files like images, etc.
		- templates - Jinja2 template (HTML pages)
		- `__init__.py` - this has init_app code
		- `forms.py` - forms if needed
		- `models.py` - database models if used
		- `routes.py` - routes (HTML pages, views) of the app
	- `app_config.py` - Flask app config file
	- `main_frontent.py` - the main Flask entry point
- **db** - database, if used
	- mockup_db.sqlite - a mockup example SQLite database with 1 simple table
- **docker** - dockerfiles. In this example we use only one container, so only 1
dockerfile.
- **tests** - tests
- `.gitignore` - you should have your own .gitignore to ignore all local IDE 
  stuff, etc.
- `config.yaml` - general config.yaml for this app
- `docker-compose.yaml` - docker compose file
- `README.md` - readme
- `requirements.txt` - requirements
   
# Quick tips

- How to make requirements.txt file
`pip install pireqs`
`pipreqs /path/to/project`
- Build image, start container and deploy the app: `docker-compose -f docker-compose.dev.yml up --build -d` 
	- -f to specify particular docker-compose yaml file
	- -d to start in deatached mode
  