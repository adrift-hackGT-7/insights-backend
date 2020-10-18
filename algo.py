from revenue import revenue

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

# for each shop calculate week over week for each of the 4 weeks (maybe look at 2 then 3 then 4)
# determine which shops had the the largest growth intraweek growth
    # determine which products in the period sold for the highest profit margins
    # determine promotions (not yet implemented but in the data)
    # recommend this item to stores with same product and lower sales in this product (% of profit this product/total profit)
     
def weekoverweek():
    receipts_file_name = "archive/201904_sales_reciepts.csv"
    sales_outlet_file_name = "archive/sales_outlet.csv"
    product_file_name = "archive/product.csv"
    week1 = revenue("2019-04-01", "2019-04-07", receipts_file_name, sales_outlet_file_name, product_file_name)
    week2 = revenue("2019-04-08", "2019-04-14", receipts_file_name, sales_outlet_file_name, product_file_name)
    week3 = revenue("2019-04-15", "2019-04-21", receipts_file_name, sales_outlet_file_name, product_file_name)
    week4 = revenue("2019-04-22", "2019-04-28", receipts_file_name, sales_outlet_file_name, product_file_name)

    # {store1 : {p1:rev1, p2:rev1, ...} ... storeN : ...}
    week1profit = week1.get_profit_dict()
    for store in week1profit:
        sum = 0
        for item in store:
            sum = sum + store[item]
        print(sum)
    
            


weekoverweek()