def test_function(fn):
    if fn.__name__ == "calculate_shipping_cost":
        test_shipping_cost(fn)
    if fn.__name__ == "calculate_driver_cost":
        test_driver_cost(fn)
    if fn.__name__ == "calculate_money_made":
        test_money_made(fn)

def test_shipping_cost(f):
    try:
        costs = f((0, 0), (1, 1))
    except TypeError:
        print("calculate_shipping_cost() did not provide default argument for shipping_type")
        return
    if not type(costs) is str:
        print("calculate_shipping_cost() did not format the result in a string")
        return
    if costs != "$1.04":
        print("calculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}".format(costs, "$1.04"))
        return
    print("OK! calculate_shipping_cost() passes tests")

class Driver:
    def __init__(self, name, speed, salary):
        self.name = name
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        string = \
            "\n\tDriver: \t{name}"\
            "\n\tSpeed: \t\t{speed}"\
            "\n\tSalary: \t{salary}"\
            .format(
                name = self.name,
                speed = self.speed,
                salary = self.salary
            )
        return string

driver1 = Driver("Josh", 2, 10)
driver2 = Driver("Alex", 7, 20)
driver3 = Driver("Hector", 9, 25)

def test_driver_cost(f):
    try:
        price, driver = f(80, driver1, driver2, driver3)
    except TypeError:
        print("calculate_driver_cost() doesn't expect multiple driver arguments")
        return
    if type(driver) is not Driver:
        print("calculate_driver_cost() did not return driver")
        return
    if price != 222.22:
        print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(price,222.22))
        return
    if driver is not driver3:
        print("calculate_driver_cost() did not provide least expensive driver")
        return
    print("OK! calculate_driver_cost() passes tests")

class Trip:
    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        driver.cost = driver_cost
        self.driver = driver

trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)

def test_money_made(f):
    try:
        money = f(UEXODI=trip1, DEFZXIE=trip2)
    except TypeError:
        print("calculate_money_made() doesn't expect multiple trip keyword arguments")
        return
    if type(money) not in (int, float):
        print("calculate_driver_cost() did not return a number")
        return
    if money != 445:
        print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(money, 445))
        return
    print("OK! calculate_money_made() passes tests")
