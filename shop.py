def min_cost(shop):
    if not shop.keys():
        return "none"
    min_total = float("inf")
    min_id = "none"
    for shop_id in shop.keys():
        total = 0
        for product in shop[shop_id].keys():
            total += shop[shop_id][product]
        if min_total > total:
            min_total = total
            min_id = shop_id
    return min_id+", "+str(min_total)


def find_shops(rows, seacrh_items):
    shop = {}
    for row in rows:
        combo = False
        for shop_product in row[2:]:
            if shop_product in seacrh_items:
                shop_id = row[0]
                price = float(row[1])
                if shop_id not in shop.keys():
                    shop[shop_id] = {}
                if not combo:
                    shop[shop_id][shop_product] = price
                    combo = True
                else:
                    shop[shop_id][shop_product] = 0
    for key in shop.keys():
        if len(shop[key]) != len(seacrh_items):
            del shop[key]
    return min_cost(shop)

import sys
import csv
with open(sys.argv[1], "r") as input_file:
    rows = csv.reader(input_file, skipinitialspace=True)
    rows = list(rows)
    search_items = sys.argv[2:]
    print find_shops(rows, search_items)
