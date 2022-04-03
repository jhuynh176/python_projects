print("--> Create Class Menu")
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        represent_string = \
        "----------------------------------------\n"\
        "{name} menu "\
        "is available from {start} to {end}.\n"\
        "--> Items include:\n{items}\n".format(
        name = self.name,
        items = self.items,
        start = self.start_time,
        end = self.end_time
        )
        return represent_string

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price += self.items[item]
        print("----------------------------")
        print("Your {menu} purchased items: \n--> {items}".format(menu = self.name, items = purchased_items))
        print("Your total cost: $" + str(total_price), "\n")
        return total_price

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

print("--> Adding menu")
print(brunch)
print(early_bird)
print(dinner)
print(kids)

brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

class Franchise:
    def __init__(self, name, address, menus):
        self.name = name
        self.address = address
        self.menus = menus

    def __repr__(self):
        string = "Restaurant {name} is located at:\n\t {address}".format(
          name = self.name,
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



flagship_store = Franchise("Flagship Store", "1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("New Installment", "12 East Mulbery Street", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))