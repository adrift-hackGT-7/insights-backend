import pandas as pd
import numpy as np


class staff:
    def __init__(self, start_date, end_date, receipts_file_name):
        # dates range/week to extract data from
        self.start_date = start_date
        self.end_date = end_date

        # to obtain the names of the necessary CSV files to read from
        self.file_name = receipts_file_name

        # values from receipts_file_name that are handy
        self.staff_per_location = {}
        self.location_list = []
        self.reading_csv_provided()

    def reading_csv_provided(self):
        # "archive/201904_sales_reciepts.csv"
        # going to assume that data needs to be sent in in this format
        # so we should have a file that showcases the metadata of the tables
        df = pd.read_csv(self.file_name, usecols=[1, 3, 4],
                         skiprows=range(2, self.start_date),
                         nrows=self.end_date-self.start_date)

        # df.loc[self.start_date:self.end_date]

        # File metadata with column numbers:
        # "transaction_id" = 0,"transaction_date" = 1,"transaction_time" = 2,
        # "sales_outlet_id" = 3,"staff_id" = 4,"customer_id" = 5,"instore_yn" = 6,
        # "order" = 7,"line_item_id" = 8,"product_id" = 9,"quantity" = 10,
        # "line_item_amount" = 11,"unit_price" = 12,"promo_item_yn" = 13

        # list of all locations
        self.location_list = df['sales_outlet_id'].unique().tolist()

        for location in self.location_list:
            # used to filter every location
            temp1 = df
            temp1 = temp1[temp1.sales_outlet_id.eq(location)]
            staff_list = temp1['staff_id'].unique().tolist()
            self.staff_per_location[location] = len(staff_list)

    def staff_at_location(self, location_id):
        return self.staff_per_location[location_id]

    def get_staff_dict(self):
        return self.staff_per_location
