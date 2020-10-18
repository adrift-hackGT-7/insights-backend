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

    #first lets calculate the week over week growth for each store for 4 weeks 
    store_weekly_data = calc_weekly_data()
    initial = 0
    fin = {}
    for i in store_weekly_data[0]:
        if i == 1:
            fin[0] = 0
        fin[i] = (store_weekly_data[i] - store_weekly_data[i-1])/store_weekly_data[i-1]
    # this is just for one store, increase it once all stores are done 

def weekoverweek():
    

    