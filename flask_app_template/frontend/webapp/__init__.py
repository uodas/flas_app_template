"""
Has init_app function to initiate the Flask app.

"""
from datetime import datetime

from flask import Flask
from flask_bootstrap import Bootstrap4 # Bootstrap for web styling
from flask_sqlalchemy import SQLAlchemy # Flask-SQLAlchemy
from flask_apscheduler import APScheduler # Flask-APScheduler
from flask_wtf import FlaskForm # module for forms

import frontend.app_config as flask_config
import backend.additional_backend as mylib
import backend.main_backend as backend

# globally accessible stuff
db = SQLAlchemy() # database
scheduler = APScheduler() #  apscheduler


def init_app(config_file_path):
    """
    Initiates the Flask app.
    
    Args:
        config_file_path, path to the main config.yaml
    Returns:
        app: initiated app 
    """   
    ### Flask app
    app = Flask(__name__, instance_relative_config=False)
    
    ### read config_file_path file
    config = mylib.read_config(config_file_path)
    
    ### prepp logger and add to the Flask app
    log = mylib.setup_logger(config['logging'], config['flask_app']['log'])    
    app.logger = log
    app.logger.info('Initializing an app.')
    app.logger.info('init_app, reading configs.')
    
    ### check main config if we are debug or prod and read in Flask config
    app_config = None
    if config['flask_app']['mode'] == 'debug':
        app_config = flask_config.DevConfig()
        app_config.read_config(config)
    elif config['flask_app']['mode'] == 'prod':
        app_config = flask_config.ProdConfig()
        app_config.read_config(config)
    
    app_config.APP_TEMPLATE = config    
    app.config.from_object(app_config) # load configs to the app    
    
    ### flask_sqlalchemy
    app.logger.info('init_app, init db.')
    db.init_app(app) # add app to database stuff
    
    ### flask_bootstrap
    app.logger.info('init_app, Bootstrap.')
    Bootstrap4(app) # add Bootstrap stuff
    
    ### flask_apscheduler ###
    app.logger.info('init_app, APScheduler.')
    scheduler.init_app(app)
    scheduler.start()
    min_interval = config['apscheduler']['check_interval_sec']
    
    #!!! here is where we start backend job in apscheduler
    job = scheduler.add_job(id='Task', 
        func=lambda: backend.log_message(app.logger, 'VILMA Template: '), 
            trigger='interval', seconds=min_interval) 
    job.modify(next_run_time=datetime.now()) # This hopefully start the job right away, before next interval

    
    with app.app_context(): # this is to get us into app's context, sort of now we have access to apps vars and all
        from frontend.webapp import routes # routes basically define webapp pages like index.html, etc.
        return app
