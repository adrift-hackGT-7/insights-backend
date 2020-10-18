import numpy as np
import pandas as pd
from staff import staff


receipts_file_name = "archive/201904_sales_reciepts.csv"
staff_obj = staff(1, 11362, receipts_file_name)

print(staff_obj.staff_at_location(3))

print(staff_obj.get_staff_dict())
