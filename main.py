from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def algo(store_id):
    # calculate best product for each store
    # calculate best promotion for each store
    # calculate month over month growth (once we expand the data that exists in the system)
        # we could do week over week instead of month over month
    