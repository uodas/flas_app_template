"""
Start the Flask app, entry point.

"""
from frontend.webapp import init_app # init_app foo is in __init__.py of webapp module


# get command line args
#args = mylib.get_args()

print('Flask APP, vilma template', __file__)

config_file_path = 'config.yaml'
app = init_app(config_file_path) # crete a flask app by running init_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    