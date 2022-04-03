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