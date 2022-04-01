"""
Write a shipping progam that 
- asks the user for the weight of their package
- tells them which method of shipping is cheapest
- how much it will cost to ship their package using the chosen shippers
"""

# Ask user for item weight
weight = float(input("Enter the weight of your package in pounds (lbs): "))

# Ground Shipping
#---------------------------------------
# Flat Charge
ground_flat = 20
if weight <= 2:
  cost_per_lb = 1.50
elif weight > 2 and weight <= 6:
  cost_per_lb = 3.00
elif weight > 6 and weight <= 10:
  cost_per_lb = 4.00
else:
  cost_per_lb = 4.75
cost_total_ground = cost_per_lb * weight + ground_flat
print ("\nGround Shipping")
print ("The Total Cost is: \t$", cost_total_ground)

# Ground Shipping Premium
#---------------------------------------
# Flat Charge
ground_premium_flat = 125.00
print ("\nGround Shipping Premium")
# Reminder: Single flat charge only
print ("Notice: This is a single flat charge!")
print ("The Total Cost is: \t$", ground_premium_flat)

# Drone Shipping
#---------------------------------------
# Flat Charge
drone_flat = 0
print("\nDrone Shipping")
if weight <= 2:
  cost_per_lb = 4.50
elif weight > 2 and weight <= 6:
  cost_per_lb = 9.00
elif weight > 6 and weight <= 10:
  cost_per_lb = 12.00
else:
  cost_per_lb = 14.25
cost_total_drone = cost_per_lb * weight + drone_flat
print ("The Total Cost is: \t$", cost_total_drone)
