"""
This is Flask app config file.

"""
import os, random, string

class BaseConfig():
    """Base config"""
    # this is needed for webforms to work, some security thing..., longish line just generates random string
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    APP_TEMPLATE = None # I just use this variable to bind to configs read from config.yaml
    
    @classmethod
    def read_config(cls, config):
        cls.SQLALCHEMY_DATABASE_URI = config['db']['sqlite_db']

class DevConfig(BaseConfig):
    """Dev config"""   
    DEBUG = True 
    TESTING = True
    
class ProdConfig(BaseConfig):
    """Prod config"""
    DEBUG = False 
    TESTING = False
        
    