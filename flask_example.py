
# Import dependencies
from flask import Flask

#  Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# First, define the starting point (ie. the root). To do this, use the function @app.route('/')
@app.route('/')
def  Hello_world():
    return 'Hello world'

# Run a Flask App in Terminal , just as shown below
#set FLASK_APP=flask_example.py
