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