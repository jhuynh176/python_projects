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