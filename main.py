from flask import Flask
import algo
import json
import make_json as make_json
from product import product
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

ALGO returns all the data, the three dictionaries
then here in routes, we look at the ID for the store requested, and return data for 
the store opposite 3->5 5->8 8->3
then we look at this data and convert to JSON
 - change numbers for locations to names
 - change numbers for products to names 
 - add in increase/decrease/staff based on data provided (which array we select from or if staff 1/2/0)

    (best_prod_per_loc_per_week)
    (worst_prod_per_loc_per_week)
    (staff_count_per_loc)

"""
location_map = {3: "Astoria", 5: "Lower Manhattan", 8: "Hell's Kitchen"}
product_file_name = "archive/product.csv"
prod_obj = product(product_file_name)


@app.route('/shop/{id}/insight/current')
def current_insight():
    ret = algo.weekoverweek()
    # return json objects for week 3-4 diffs
    # look at store 5 looking at data for store 3
    best_prod = ret[0][3][2]
    worst_prod = ret[1][3][2]
    staff_count = ret[2][3][2]

    # get name of best product
    # get name for worst product
    # get increase or decrease staff
    staff_item = None
    if staff_count == 1:
        staff_item = make_json.make_item(
            "increase-staffing", "people", "accepted", "Accepted - increase staffing to see potential revenue increases", "")
    if staff_count == 2:
        staff_item = make_json.make_item(
            "decrease-staffing", "people", "accepted", "Accepted - decrease staffing to see potential revenue increases", "")

    best_prod_name = prod_obj.get_prod_name(best_prod)
    best_item = make_json.make_item(
        best_prod_name, "add", "accepted", "Add *{0}* to your catalog for an increased revenue".format(best_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")

    worst_prod_name = prod_obj.get_prod_name(worst_prod)
    worst_item = make_json.make_item(
        worst_prod_name, "remove", "dismissed", "Remove *{0}* from your catalog for an increased revenue".format(worst_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")

    temp = []
    # temp.append(staff_item)
    temp.append(best_item)
    temp.append(worst_item)
    one = make_json.make_group_element(temp, "catalog", "Catalog")

    temp = []
    temp.append(staff_item)
    two = make_json.make_group_element(temp, "staffing", "Staffing")

    temp = []
    temp.append(one)
    temp.append(two)

    return json.dumps(make_json.make_group(temp))


@app.route('/shop/{id}/insight/past')
def past_insight():
    ret = algo.weekoverweek()
    # return json objects for week 3-4 diffs
    # look at store 5 looking at data for store 3
    best_prod = ret[0][3][0]
    worst_prod = ret[1][3][0]
    staff_count = ret[2][3][0]

    # get name of best product
    # get name for worst product
    # get increase or decrease staff
    staff_item = None
    if staff_count == 1:
        staff_item = make_json.make_item(
            "increase-staffing", "people", "accepted", "Accepted - increase staffing to see potential revenue increases", "")
    if staff_count == 2:
        staff_item = make_json.make_item(
            "decrease-staffing", "people", "accepted", "Accepted - decrease staffing to see potential revenue increases", "")

    best_prod_name = prod_obj.get_prod_name(best_prod)
    best_item = make_json.make_item(
        best_prod_name, "add", "accepted", "Add *{0}* to your catalog for an increased revenue".format(best_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")

    worst_prod_name = prod_obj.get_prod_name(worst_prod)
    worst_item = make_json.make_item(
        worst_prod_name, "remove", "dismissed", "Remove *{0}* from your catalog for an increased revenue".format(worst_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")

    temp = []
    temp.append(staff_item)
    temp.append(best_item)
    temp.append(worst_item)
    one = make_json.make_group_element(temp, "march 2019", "March 2019")

    # return json objects for week 3-4 diffs
    # look at store 5 looking at data for store 3
    best_prod = ret[0][3][1]
    worst_prod = ret[1][3][1]
    staff_count = ret[2][3][1]

    # get name of best product
    # get name for worst product
    # get increase or decrease staff
    temp = []
    staff_item = None
    if staff_count == 1:
        staff_item = make_json.make_item(
            "increase-staffing", "people", "accepted", "Accepted - increase staffing to see potential revenue increases", "")
    if staff_count == 2:
        staff_item = make_json.make_item(
            "decrease-staffing", "people", "accepted", "Accepted - decrease staffing to see potential revenue increases", "")

    best_prod_name = prod_obj.get_prod_name(best_prod)
    best_item = make_json.make_item(
        best_prod_name, "add", "accepted", "Add *{0}* to your catalog for an increased revenue".format(best_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")

    if (worst_prod != 0):
        worst_prod_name = prod_obj.get_prod_name(worst_prod)
        worst_item = make_json.make_item(
            worst_prod_name, "remove", "dismissed", "Remove *{0}* from your catalog for an increased revenue".format(worst_prod_name), "Based on sales data in similar stores that stock this item in the past 2 months")
        temp.append(worst_item)

    temp.append(staff_item)
    temp.append(best_item)
    two = make_json.make_group_element(temp, "february 2019", "February 2019")

    temp = []
    temp.append(one)
    temp.append(two)

    return json.dumps(make_json.make_group(temp))
