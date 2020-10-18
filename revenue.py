import numpy as np 
import pandas as pd
# sum by product_id and sales_outlet_id
# find individual product profits and 
# overall profits at a location

class revenue:
    def __init__(self, start_date, end_date, receipts_file_name, sales_outlet_file_name, product_file_name):
        # dates range/week to extract data from
        self.start_date = start_date
        self.end_date = end_date

        # to obtain the names of the necessary CSV files to read from
        self.file_name = receipts_file_name
        self.sales_outlet_file_name = sales_outlet_file_name
        self.product_file_name = product_file_name

        # values from receipts_file_name that are handy
        self.revenue_per_location = {}
        self.product_ids = []
        self.location_list = []
        self.reading_csv_provided()

        # values from salues_outlet_file_name that are handy
        self.sales_outlet_to_id = {}
        self.reading_sales_outlet_csv()

        # values from product_file_name that are handy
        self.product_to_id = {}
        self.reading_product_csv()

        # values for profit calculation
        self.profit_per_location = {}
        self.profit_per_product()

    def reading_csv_provided(self):
        # "archive/201904_sales_reciepts.csv"
        # going to assume that data needs to be sent in in this format
        # so we should have a file that showcases the metadata of the tables
        df = pd.read_csv(self.file_name, usecols = [1, 3, 9, 10, 12, 13])
        df.loc[self.start_date:self.end_date]

        # File metadata with column numbers:
        # "transaction_id" = 0,"transaction_date" = 1,"transaction_time" = 2,
        # "sales_outlet_id" = 3,"staff_id" = 4,"customer_id" = 5,"instore_yn" = 6,
        # "order" = 7,"line_item_id" = 8,"product_id" = 9,"quantity" = 10,
        # "line_item_amount" = 11,"unit_price" = 12,"promo_item_yn" = 13

        # total revenue note, we have to multiply by the quantity
        # print((df['quantity']*df['unit_price']).sum())

        # to find the revenue for each product
        self.product_ids = df['product_id'].unique().tolist()
        # list of all locations
        self.location_list = df['sales_outlet_id'].unique().tolist()

        for location in self.location_list:
            # used to filter every location
            temp1 = df
            temp1 = temp1[temp1.sales_outlet_id.eq(location)]
            revenue_per_product = {}
            for id in self.product_ids:
                # used to filter data for every product
                temp2 = temp1
                temp2 = temp2[temp2.product_id.eq(id)]
                revenue_per_product[id] = round((temp2['quantity']*temp2['unit_price']).sum(), 3)
            self.revenue_per_location[location] = revenue_per_product

    def reading_sales_outlet_csv(self):
        # Sales Outlet CSV metadata:
        # sales_outlet_id = 0,sales_outlet_type = 1,store_square_feet = 2,
        # store_address = 3,store_city = 4,store_state_province = 5,
        # store_telephone = 6,store_postal_code = 7,store_longitude = 8,
        # store_latitude,manager = 9,Neighorhood = 10
    
        # here Neighborhood is basically the store name
        # I just need to get a mapping from name to ID
        sales_outlet = pd.read_csv(self.sales_outlet_file_name, usecols = [0, 10])
        zipper = zip(sales_outlet['Neighborhood'].unique().tolist(), sales_outlet['sales_outlet_id'].unique().tolist())

        for i in zipper():
            self.sales_outlet_to_id[i[0]] = i[1]

    def reading_product_csv(self):
        # Product CSV metadata:
        # product_id = 0,product_group = 1,product_category = 2,product_type,product = 3,
        # product_description = 4,unit_of_measure = 5,current_wholesale_price = 6,
        # current_retail_price = 7,tax_exempt_yn = 8,promo_yn = 9,new_product_yn = 10

    
        # here product is the name that will be passed in
        # I just need to get a mapping from name to ID
        products = pd.read_csv(self.product_file_name, usecols = [0, 3])
        zipper = zip(products['product'].unique().tolist(), products['product_id'].unique().tolist())

        for i in zipper():
            self.product_to_id[i[0]] = i[1]

    def revenue_for_location(self, location):
        # the location here is a name, so we need to use the mapping to find the relevant stuff
        location_id = self.sales_outlet_to_id[location]
        product_mapping = self.revenue_per_location[location_id]
        return sum(product_mapping.values())

    def revenue_for_product_at_location(self, location, product):
        # the location here is a name, so we need to use the mapping to find the relevant stuff
        location_id = self.sales_outlet_to_id[location]
        # the product here is a name, so we need to use the mapping to find the relevant stuff
        product_id = self.product_to_id[product]

        product_mapping = self.revenue_per_location[location_id]
        return product_mapping[product_id]

    #____________________________________________________________________________________________________
    # methods for calculating profits

    def profit_per_product(self):
        # for each product, look up the wholesale price in 
        # product.csv (current_wholesale_price) 
        # we can subtract (price we charge - current_wholesale_price)
        # and then multiply by quantity to calculate profit
        df = pd.read_csv(self.file_name, usecols = [3, 9, 10])
        df.loc[start_date:end_date]
        df2 = pd.read_csv(self.product_file_name, usecols = [0 , 6])
        for location in self.location_list:
            # used to filter every location
            temp1 = df
            temp1 = temp1[temp1.sales_outlet_id.eq(location)]
            profit_per_product = {}
            for id in self.product_ids:
                # used to filter data for every product
                temp2 = temp1
                temp2 = temp2[temp2.product_id.eq(id)]
                temp3 = df2[df2.product_id.eq(id)]
                profit_per_product[id] = round((temp2['quantity']*temp3['current_wholesale_price']).sum(), 3)
            self.profit_per_location[location] = profit_per_product

    def profit_for_location(self, location):
        # the location here is a name, so we need to use the mapping to find the relevant stuff
        location_id = self.sales_outlet_to_id[location]
        product_mapping = self.profit_per_location[location_id]
        return sum(product_mapping.values())

    def profit_for_product_at_location(self, location, product):
        # the location here is a name, so we need to use the mapping to find the relevant stuff
        location_id = self.sales_outlet_to_id[location]
        # the product here is a name, so we need to use the mapping to find the relevant stuff
        product_id = self.product_to_id[product]

        product_mapping = self.profit_per_location[location_id]
        return product_mapping[product_id]

    #____________________________________________________________________________________________________
    # to obtain the dictionaries for revenue and profit
    def get_revenue_dict(self):
        return self.revenue_per_location

    def get_profit_dict(self):
        return self.profit_per_location