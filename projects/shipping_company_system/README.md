# Shipping Company System

## Introduction
- Create a program that able to:
    - calculate shipping cost
    - calculate driver cost
        - find cheapest driver
        - find cheapest driver cost
    - calculate money made
    -
## Description
- `class`
    - Driver
        - speed
        - salary
- `dictionary`
    - Shipping Price 
        - shipping type : shipping rate
- `functions`
    - `get_distance` 
        - calculate distance using provided latitude and longtitude from the start location to end location
    - `calculate_shipping_cost`
        - get distance
        - get shipping rate
        - return price
    - `calculate_driver_cost`
        - get list of drivers, and their information
        - compare all drivers
        - find cheapest driver
        - find cheapest driver cost
    - `calculate_money_made`
        - calculate the total revenue from all trips
- `test functions`
    - `test_shipping_cost`
    - `test_driver_cost`
    - `test_revenue_made`

## Output
```
OK! calculate_shipping_cost() passes tests
OK! calculate_driver_cost() passes tests
UEXODI
DEFZXIE
OK! calculate_money_made() passes tests
```
```
SYSTEM: Calculating driver cost
-------------------------------------
Found FIRST driver:
        Driver:       Josh
        Speed:        2
        Salary:       10
        Total Cost:   $400.0

-------------------------------------
Found CHEAPER driver:
        Driver:       Alex
        Speed:        7
        Salary:       20
        Total Cost:   $228.57

-------------------------------------
Found CHEAPER driver:
        Driver:       Hector
        Speed:        9
        Salary:       25
        Total Cost:   $222.22
```
