# Restaurant Table Handling System

## Introduction
- Create a simple restaurant application that able to:
    - store the orders
    - store occupied customers
    - store bill
    - send order to kitchen

## Description
- `dictionary`
    - list of tables
        - table number
        - customer
        - vip status
        - ordered items
- `function`
    - `table_status` - return status of all tables
    - `assign_table` - assign customer to a table
    - `assign_order` - assign ordered items to the table

## Output
- Table status
```
SYSTEM:
-----------------------------------
Current table status:
1 : {}
2 : {}
3 : {}
4 : {}
5 : {}
6 : {}
7 : {}

```
- Assign table
```
-----------------------------------
Customer: Jiho
	Has entered table 1.
	VIP = False.

-----------------------------------
Customer: Arwa
	Has entered table 2.
	VIP = True.

-----------------------------------
Customer: Isa
	Has entered table 3.
	VIP = False.

SYSTEM:
-----------------------------------
Current table status:
1 : {'name': 'Jiho', 'vip_status': False, 'order': ''}
2 : {'name': 'Arwa', 'vip_status': True, 'order': ''}
3 : {'name': 'Isa', 'vip_status': False, 'order': ''}
4 : {}
5 : {}
6 : {}
7 : {}

```
- Assign ordered items
```
-----------------------------------
Table 2 has ordered items:
         Steak, Seabass, Wine Bottle
Sending order to kitchen.

-----------------------------------
Table 1 has ordered items:
         Hamburgur, Soup, Soda
Sending order to kitchen.

-----------------------------------
Table 3 has ordered items:
         Pancakes, Orange Juice, Apple Juice
Sending order to kitchen.
```
- Order Status
```
SYSTEM:
-----------------------------------
Table 1 requests Order Status:
         Food : Hamburgur, Soup
         Drinks : Soda
Items are being made.

SYSTEM:
-----------------------------------
Table 3 requests Order Status:
         Food : Pancakes
         Drinks : Orange Juice, Apple Juice
Items are being made.
```
- Current table status
```
SYSTEM:
-----------------------------------
Current table status:
1 : {'name': 'Jiho', 'vip_status': False, 'order': {'food': 'Hamburgur, Soup', 'drinks': 'Soda'}}
2 : {'name': 'Arwa', 'vip_status': True, 'order': {'food': 'Steak, Seabass', 'drinks': 'Wine Bottle'}}
3 : {'name': 'Isa', 'vip_status': False, 'order': {'food': 'Pancakes', 'drinks': 'Orange Juice, Apple Juice'}}
4 : {}
5 : {}
6 : {}
7 : {}
```