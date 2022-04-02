# Game Night - Event Party Planning

## Introduction
- You want to celebrate a game night event.
- Conditions:
    - If you pick the wrong night, not enough people will come, and game night will be cancelled.
- Task:
    - `Design` two game nights
    - `Automate` the process for selecting game night base on:
        - First night: Most availability
        - Second night: Back-up secondary availability

## Description
- `Dictionary`
    - `key`: name, availability_day
    - `value`: string_name , list_of_day
- `Functions`
    - `add_gamer` - adding gamer
    - `build_daily_frequency_table` - create table to keep track of availability day
    - `calculate_availability` - count each day, then add to the frequency table
    - `find_best_night` - select the best night base on highest number in frequency table
    - `available_on_night` 
        - automate the process of picking gamers that available on the best night
        - add to list
    - `form_email` - creating default email format
    - `send_email` - send formated email to chosen list of available gamers
    - `unable_to_attend_best_night` - create a secondary gamer night

## Output
```
>>> Calling add_gamer()
        Gamer 1 :        {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
        Gamer 2 :        {'name': 'Thomas Nelson', 'availability': ['Tuesday', 'Thursday', 'Saturday']}
        Gamer 3 :        {'name': 'Joyce Sellers', 'availability': ['Monday', 'Wednesday', 'Friday', 'Saturday']}
        Gamer 4 :        {'name': 'Michelle Reyes', 'availability': ['Wednesday', 'Thursday', 'Sunday']}
        Gamer 5 :        {'name': 'Stephen Adams', 'availability': ['Thursday', 'Saturday']}
        Gamer 6 :        {'name': 'Joanne Lynn', 'availability': ['Monday', 'Thursday']}
        Gamer 7 :        {'name': 'Latasha Bryan', 'availability': ['Monday', 'Sunday']}
        Gamer 8 :        {'name': 'Crystal Brewer', 'availability': ['Thursday', 'Friday', 'Saturday']}
        Gamer 9 :        {'name': 'James Barnes Jr.', 'availability': ['Tuesday', 'Wednesday', 'Thursday', 'Sunday']}
        Gamer 10 :       {'name': 'Michel Trujillo', 'availability': ['Monday', 'Tuesday', 'Wednesday']}

>>> Calling build_daily_frequency_table()

>>> Calling count_availability()
    Frequency Table:
         {'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}

>>> Calling find_best_night()
    Gamers are most available in: Thursday, with 6 people
    Gamer night will be celebrated on --> Thursday
    
    List of gamers available on Thursday are:
         {'name': 'Thomas Nelson', 'availability': ['Tuesday', 'Thursday', 'Saturday']}
         {'name': 'Michelle Reyes', 'availability': ['Wednesday', 'Thursday', 'Sunday']}
         {'name': 'Stephen Adams', 'availability': ['Thursday', 'Saturday']}
         {'name': 'Joanne Lynn', 'availability': ['Monday', 'Thursday']}
         {'name': 'Crystal Brewer', 'availability': ['Thursday', 'Friday', 'Saturday']}
         {'name': 'James Barnes Jr.', 'availability': ['Tuesday', 'Wednesday', 'Thursday', 'Sunday']}
```
```
__________________________________________

Hi Kimberly Warner,

The Gamers's Club is happy to host "Elden Ring" night and wishes you will attend.
Come by on Monday and have a blast!

Happy Gaming,
Gamer's Club

==========================================
__________________________________________

Hi Joyce Sellers,

The Gamers's Club is happy to host "Elden Ring" night and wishes you will attend.
Come by on Monday and have a blast!

Happy Gaming,
Gamer's Club

==========================================
```
