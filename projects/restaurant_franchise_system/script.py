print("--> Creating Menu class\n")
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
  #   represent_string = \
  # "{name} menu "\
  # "is available from {start} to {end}.\n"\
  # "Items include:\n\t{items}\n".format(
  #   name = self.name,
  #   items = self.items,
  #   start = self.start_time,
  #   end = self.end_time
  # )
    represent_string = \
    "{name} menu "\
    "is available from {start} to {end}.\n".format(
      name = self.name,
      start = self.start_time,
      end = self.end_time
    )
    return represent_string

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    print("----------------------------")
    print("Your {menu} purchased items: \n\t{items}".format(menu = self.name, items = purchased_items))
    print("Your total cost: $" + str(total_price), "\n")
    return total_price

print("--> Adding menu\n")
arepas_menu = Menu(
  "Take a\' Arepa",
  {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
  },
  10,
  20
)
brunch = Menu(
  "Brunch",
  {  
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
  } ,
  11,
  16
)

early_bird = Menu(
  "Early_bird",
  {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00
  },
  15,
  18
)

dinner = Menu(
  "Dinner",
  {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
  },
  17,
  23
)

kids = Menu(
  "Kids",
  {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
  },
  11,
  21
)

print(arepas_menu)
print(brunch)
print(early_bird)
print(dinner)
print(kids)

brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

print("--> Creating Franchise class\n")
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        string = "Franchise located at: {address}".format(
          address = self.address
          )
        return string

    def available_menus(self, time):
        print("\nThese menu are available at", time, ":")
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
              available_menu.append(menu.name)
        if available_menu != []:
          return available_menu
        return print("There is no menu available at {time}.".format(time = time))

print("--> Adding franchises\n")
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulbery Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu] )

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

print("\n--> Creating Business class")
class Business:
    def __init__(self, name, franchises):
      self.name = name
      self.franchises = franchises

    def __repr__(self):
      string = \
      "\n{name}\'s business includes: \n"\
      "{franchises}".format(
        name = self.name, 
        franchises = self.franchises
        )
      return string

print("\n--> Adding business")
basta_fazoolin = Business("Basta Fazoolin\' with my Heart", [flagship_store, new_installment])
arepas_business = Business("Take a\' Arepa", [arepas_place])

print(basta_fazoolin)
print(arepas_business)



