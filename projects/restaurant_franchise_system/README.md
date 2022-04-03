# Restaurant Franchise System

## Introduction
- This project will create a restaurant system, populate with menus and functions to keep it running.
- Then we will create several franchises that operated on the oringal restaurant system.

## Description
- `class` Restaurant
    - `constructor`
        - name
        - menu_items = `dictionary {'name': price}`
        - start_time
        - end_time
    - `representation` showcase the created paremeters upon calling
    - `calculate_bill` return total prices for all purchased item
- `class` Franchise
    - `constructor` 
        - address 
        - menus = class
    - `available_menus`
        - show case menus that available during current calling time
- `class` Business
    - `constructor`
        - name
        - franchise = class

## Output
Menu Class
```
python .\script.py
--> Creating Menu class
--> Adding menu

Take a' Arepa menu is available from 10 to 20.

Brunch menu is available from 11 to 16.

Early_bird menu is available from 15 to 18.

Dinner menu is available from 17 to 23.

Kids menu is available from 11 to 21.

----------------------------
Your Brunch purchased items:
        ['pancakes', 'home fries', 'coffee']
Your total cost: $13.5

----------------------------
Your Early_bird purchased items:
        ['salumeria plate', 'mushroom ravioli (vegan)']
Your total cost: $21.5
```
Franchise Class
```
--> Creating Franchise class
--> Adding franchises

Franchise located at: 1232 West End Road
Franchise located at: 12 East Mulbery Street

These menu are available at 12 :
['Brunch', 'Kids']

These menu are available at 17 :
['Early_bird', 'Dinner', 'Kids']
```
Business Class
```
--> Creating Business class
--> Adding business

Basta Fazoolin' with my Heart's business includes:
[Franchise located at: 1232 West End Road, Franchise located at: 12 East Mulbery Street]
Take a' Arepa's business includes:
[Franchise located at: 189 Fitzgerald Avenue]
```
