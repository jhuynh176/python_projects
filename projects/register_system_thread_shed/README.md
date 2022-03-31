# Register System - Thread Shed

## Introduction
- Your daily responsibilities involve:
	- tallying the number of sales during the day
	- calculating the total amount of money made
	- keeping track of the names of the customers

## Description
 - Unfortunately, the system has an extremely outdated register system and stores all of the transaction information in one huge unwieldy string called daily_sales.
 - All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale is all recorded in this same string. 
 - Your tasks are:
 	- iterate string
 	- clean up each transaction
 	- store all the information in easier-to-access lists

# Output
```
Original: 
Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   , 
. . . 
. . . 

After Clean Up:

Customers:
 ['Edith Mcbride', 'Herbert Tran', 'Paul Clarke', 'Lucille Caldwell', 'Eduardo George', 'Danny Mclaughlin', 'Stacy Vargas', 'Shaun Brock', 'Erick Harper', 'Michelle Howell', 'Carroll Boyd', 'Teresa Carter', 'Jacob Kennedy', 'Craig Chambers', 'Peggy Bell', 'Kenneth Cunningham', 'Marvin Morgan', 'Marjorie Russell', 'Israel Cummings', 'June Doyle', 'Jaime Buchanan', 'Rhonda Farmer', 'Darren Mckenzie', 'Rufus Malone', 'Hubert Miles', 'Joseph Bridges', 'Sergio Murphy', 'Audrey Ferguson', 'Edna Williams', 'Randy Fleming', 'Elisa Hart', 'Ernesto Hunt', 'Shannon Chavez', 'Sammy Cain', 
 . . .

Sales:
 ['$1.21', '$7.29', '$12.52', '$5.13', '$20.39', '$30.82', '$1.85', '$17.98', '$17.41', '$28.59', '$14.51', '$19.64', '$11.40', '$8.79', '$8.65', '$10.53', '$16.49', '$6.55', '$11.86', '$22.29', '$8.35', '$2.91', '$22.94', '$4.70', '$3.59', '$5.66', '$17.51', '$5.54', '$17.13', '$21.13', '$0.35', '$13.91', 
. . . 

Thread sold:
 ['white', 'white', 'blue', 'white', 'blue', 'white', 'white', 'yellow', 'purple', 'purple', 'yellow', 'purple', 'yellow', 'blue', 'blue', 'purple', 'blue', 'white', 'white', 'red', 'white', 'blue', 'red', 'blue', 'green', 'blue', 'green', 'blue', 'red', 'green', 'blue', 'red', 'black', 'black', 'yellow', 'white', 'black', 'yellow', 'white', 'black', 'yellow', 'green', 'green', 'yellow', 'green', 'yellow', 'blue', 'green', 'yellow', 'purple'
 . . .
 . . .

Red thread, there are 24 sales today.
Yellow thread, there are 34 sales today.
Green thread, there are 30 sales today.
White thread, there are 28 sales today.
Black thread, there are 26 sales today.
Blue thread, there are 22 sales today.
Purple thread, there are 17 sales today.

Total sales: $1498.74

Total customers: 100

Total thread sold: 181

Average cost per customer: $14.99
```