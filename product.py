import pandas as pd
import numpy as np


class product:
    def __init__(self, product_file_name):
        self.product_file_name = product_file_name
        self.prod_map = {}

        # values from receipts_file_name that are handy
        self.staff_per_location = {}
        self.location_list = []
        self.reading_csv_provided()

    def reading_csv_provided(self):
        products = pd.read_csv(self.product_file_name, usecols=[0, 4])
        prod_name = products['product'].unique().tolist()
        prod_ids = products['product_id'].unique().tolist()
        zipper = zip(prod_name, prod_ids)

        for prod, id in zipper:
            self.prod_map[id] = prod

    def get_prod_name(self, id):
        return self.prod_map[id]

    def get_prod_map(self):
        return self.prod_map
