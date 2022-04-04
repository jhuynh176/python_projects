from ast import FloorDiv
from traceback import TracebackException


tables = {
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

def table_status():
    print(\
    "\nSYSTEM:\n-----------------------------------"\
    "\nCurrent table status:")
    for table, info in tables.items():
        print(table, ':', info)

def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}

    print(\
    "\n-----------------------------------"\
    "\nCustomer: {name}"\
    "\n\tHas entered table {table_number}."\
    "\n\tVIP = {status}."\
    .format(
        table_number = table_number,
        name = name,
        status = vip_status
        ))

# Write your code below: 
def assign_food_items(table_number, **order_items):
    food = order_items['food']
    drinks = order_items['drinks']

    # tables[table_number]['order'] = order_items
    tables[table_number]['order']['food'] = food
    tables[table_number]['order']['drinks'] = drinks

    print(\
    "\n-----------------------------------"\
    "\nTable {table} has ordered items:"\
    "\n\t{food}, {drinks}"\
    .format(
        table = table_number,
        food = food,
        drinks = drinks
        )
    )
    print("Sending order to kitchen.")


def order_status(table_number):
    print("\nSYSTEM:\n-----------------------------------")
    print("Table {table} requests Order Status:"\
        .format(table = table_number))
    # Method 1:
    # for key, value in order_items.items():
    #     print('\t', key.title(), ':', value)
    
    # Method 2:
    for key, value in tables[table_number]['order'].items():
        print('\t', key.title(), ':', value)
    print("Items are being made.")

table_status()

assign_table(1, 'Jiho', False)
assign_table(2, 'Arwa', True)
assign_table(3, 'Isa', False)

table_status()

assign_food_items(2, food = 'Steak, Seabass', drinks = 'Wine Bottle')

assign_food_items(1, food = 'Hamburgur, Soup', drinks = 'Soda')

assign_food_items(3, food = 'Pancakes', drinks = 'Orange Juice, Apple Juice')

order_status(2)
order_status(1)
order_status(3)

table_status()