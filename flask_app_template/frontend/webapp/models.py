'''Database models (tables).
'''

from frontend.webapp import db

class Data(db.Model):
    """A Class representing 'Guys' table in the database.
    """
    # @todo: take table name from the main config.yaml
    __tablename__ = 'Guys'
        
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String)
    Surname = db.Column(db.Boolean, default = True)
    Status = db.Column(db.String)
    Level = db.Column(db.String)
    
    
        