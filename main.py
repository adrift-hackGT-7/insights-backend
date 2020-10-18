from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
list of routes
    - /shop/{id}/insight/current
        - returns current insights for a shop
    - /shop/{id}/insight/past
        - returns past insights for a shop

    - /shop/{id} 
        - returns the week over week growth for a shop
"""

@app.route('/shop/{id}/insight/current')
def current_insight():
    return 'Hello, World!'

@app.route('/shop/{id}/insight/past')
def past_insight():
    return 'Hello, World!'


    