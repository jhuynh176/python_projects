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

