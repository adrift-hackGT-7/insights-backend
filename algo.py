from revenue import revenue
from datetime import datetime
import pandas as pd


def algo(store_id):
    # calculate best product for each store
    # calculate best promotion for each store
    # calculate month over month growth (once we expand the data that exists in the system)
    # we could do week over week instead of month over month

    # first lets calculate the week over week growth for each store for 4 weeks
    store_weekly_data = calc_weekly_data()
    initial = 0
    fin = {}
    for i in store_weekly_data[0]:
        if i == 1:
            fin[0] = 0
        fin[i] = (store_weekly_data[i] - store_weekly_data[i-1]) / \
            store_weekly_data[i-1]
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

    weeks = {}
    weeks[0] = revenue(1, 11362, receipts_file_name,
                       sales_outlet_file_name, product_file_name)
    weeks[1] = revenue(11363, 23713, receipts_file_name,
                       sales_outlet_file_name, product_file_name)  # 2019-04-08 #2019-04-14
    weeks[2] = revenue(23714, 36473, receipts_file_name,
                       sales_outlet_file_name, product_file_name)  # 2019-04-15 #2019-04-21
    weeks[3] = revenue(36474, 48427, receipts_file_name,
                       sales_outlet_file_name, product_file_name)  # 2019-04-22 #2019-04-28
    rev_by_week = {}
    for i in range(len(weeks)):
        # week -> store -> revenue for that week
        weekly_rev_by_store = {}
        for store in weeks[i].get_revenue_dict():
            sum = 0
            for item in weeks[i].get_revenue_dict()[store]:
                sum = sum + weeks[i].get_revenue_dict()[store][item]
            weekly_rev_by_store[store] = sum
        rev_by_week[i] = weekly_rev_by_store
    # print(rev_by_week)

    # growth = {}
    # for i in range(len(profits) - 1):
    #     for store in profits[i + 1]:
    #         print(store)
    #         growth[store][i + 1] = (profits[i + 2][store] -
    #                                 profits[i + 1][store])/profits[i + 1][store]
    # print(growth)

    # my list of locations --> get_locations_list
    # store -> revenue for every week
    growth_per_store = {}
    for loc in weeks[1].get_locations_list():
        growth = {}
        for i in range(len(weeks) - 1):
            growth[i] = (rev_by_week[i + 1][loc] -
                         rev_by_week[i][loc])/rev_by_week[i][loc]
        growth_per_store[loc] = growth
    # print(growth_per_store)

    # for every store I look at it on a weekly basis
    # determine the highest ratio

    # loc -> week -> best prod_id
    best_prod_per_loc_per_week = {}
    for loc in weeks[1].get_locations_list():
        week_perf = []
        for i in range(len(weeks)-1):
            prod_performance1 = weeks[i].get_revenue_dict()
            prod_performance1 = prod_performance1[loc]

            prod_performance2 = weeks[i+1].get_revenue_dict()
            prod_performance2 = prod_performance2[loc]

            # prod_id -> ratio
            ratios = {}

            for prod in prod_performance2:
                if prod not in prod_performance1.keys():
                    continue
                else:
                    ratios[prod] = (
                        prod_performance2[prod] - prod_performance1[prod])/prod_performance2[prod]
            max_ratio = max(ratios.values())
            best_prod_id = None
            for k, v in ratios.items():
                if v == max_ratio:
                    best_prod_id = k
                    break

            week_perf.append(best_prod_id)
        best_prod_per_loc_per_week[loc] = week_perf
    print(best_prod_per_loc_per_week)

    # loc -> week -> best prod_id
    best_prod_per_loc_per_week_min = {}
    for loc in weeks[1].get_locations_list():
        week_perf = []
        for i in range(len(weeks)-1):
            prod_performance1 = weeks[i].get_revenue_dict()
            prod_performance1 = prod_performance1[loc]

            prod_performance2 = weeks[i+1].get_revenue_dict()
            prod_performance2 = prod_performance2[loc]

            # prod_id -> ratio
            ratios = {}

            for prod in prod_performance2:
                if prod not in prod_performance1.keys():
                    continue
                else:
                    ratios[prod] = (
                        prod_performance2[prod] - prod_performance1[prod])/prod_performance2[prod]
            min_ratio = min(ratios.values())
            worst_prod_id = None
            for k, v in ratios.items():
                if v == min_ratio:
                    worst_prod_id = k
                    break

            week_perf.append(worst_prod_id)
        best_prod_per_loc_per_week_min[loc] = week_perf
    print(best_prod_per_loc_per_week_min)


weekoverweek()
