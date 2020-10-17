import numpy as np 
import pandas as pd
# sum by product_id and sales_outlet_id
# find individual product profits and 
# overall profits at a location

class revenue:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading_csv_provided(self):
        # "archive/201904_sales_reciepts.csv"
        # going to assume that data needs to be sent in in this format
        # so we should have a file that showcases the metadata of the tables
        df = pd.read_csv(self.file_name, usecols = [1, 3, 9, 10, 12, 13])

        # File metadata with column numbers:
        # "transaction_id" = 0,"transaction_date" = 1,"transaction_time" = 2,
        # "sales_outlet_id" = 3,"staff_id" = 4,"customer_id" = 5,"instore_yn" = 6,
        # "order" = 7,"line_item_id" = 8,"product_id" = 9,"quantity" = 10,
        # "line_item_amount" = 11,"unit_price" = 12,"promo_item_yn" = 13

        # total revenue note, we have to multiply by the quantity
        # print((df['quantity']*df['unit_price']).sum())

        # to find the revenue for each product
        product_ids = df['product_id'].unique().tolist()
        # list of all locations
        location_list = df['sales_outlet_id'].unique().tolist()

        revenue_per_location = {}

        for location in location_list:
            # used to filter every location
            temp1 = df
            temp1 = temp1[temp1.sales_outlet_id.eq(location)]
            revenue_per_product = {}
            for id in product_ids:
                # used to filter data for every product
                temp2 = temp1
                temp2 = temp2[temp2.product_id.eq(id)]
                revenue_per_product[id] = round((temp2['quantity']*temp2['unit_price']).sum(), 3)
            revenue_per_location[location] = revenue_per_product

    def revenue_for_location(self, location):


    def revenue_for_product_at_location(self, location, product):
