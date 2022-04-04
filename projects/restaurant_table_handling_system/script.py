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
  "\n-----------------------------------"\
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
def assign_and_print_order(table_number, **order_items):
  tables[table_number]['order'] = order_items

  print(\
  "\n-----------------------------------"\
  "\nTable {table} has ordered items:"\
  .format(table = table_number))

  for key, value in order_items.items():
    print('\t', key, ':', value)

  print("Sending order to kitchen.")

table_status()

assign_table(1, 'Jiho', False)
assign_table(2, 'Arwa', True)
assign_table(3, 'Isa', False)

table_status()

assign_and_print_order(2, 
  food = ['Steak', 'Seabass'], drink = ['Wine Bottle'])
assign_and_print_order(1,
  food = ['Hamburgur', 'Soda', 'Soup'])

table_status()