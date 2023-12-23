"""
Pages of the app (known as routes, views).
"""
import sqlalchemy, os
from flask import render_template
from flask import current_app as appfrom . import db
from frontend.webapp.models import Data   
from frontend.webapp.forms import AppTemplateForm
from flask.helpers import send_from_directory
    
    
"""
path to folder with the file to download
"""
download_dir = os.path.dirname(app.config['APP_TEMPLATE']['logging']
    ['handlers']['file']['filename'])
    
@app.route('/', methods=['POST', 'GET'])
def main():
    """
    Main app page. Gets latest data from the database and displays it in an HTML table.
    Args:
    Returns:
        Returns jinja template with latest data displayed in a table 
    """   
    
    template_form = AppTemplateForm()
    if template_form.validate_on_submit():
        data = template_form.data
      
        return render_template('result.jinja2', data=data)
    
    try: 
        # Querying with SQLalchemy :)
        data = db.session.execute(db.select(Data).order_by(Data.Level.desc())).scalars().all()  
    except sqlalchemy.exc.OperationalError as ex : # this happens when we can't access the database_, e.g. database_ file doesn't exist
        error = 'Can\'t access the database.'
        return render_template('error.jinja2', error=error, ex=ex)
    
    return render_template('main.jinja2', template_form=template_form, data=data)

@app.route('/result/<data>', methods=['GET'])
def result(data):
    """
    Just renders Results page. 
    Args:
        data (dict): data to display
    Return:
        renders result page with provided data
    """
    return render_template('result.jinja2', data=data)

@app.route('/files', methods=['GET'])
def files():
    """
    Page that allows to download files.
    """
    list_of_files = os.listdir(download_dir)
    
    return render_template('files.jinja2', files=list_of_files)

@app.route('/help', methods=['GET'])
def help():
    """
    Just some help text :)
    """
    return render_template('help.jinja2')
    
@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    This foo is needed to download a file.
    """
    return send_from_directory(os.getcwd()+os.sep+download_dir, filename, as_attachment=True)

