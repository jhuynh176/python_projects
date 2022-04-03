# Robot Handling System

## Introduction
- You have decided to use your programming knowledge to create a new robotics company. 
- Your idea for micro driving robots are able to:
    - pick up 
    - deliver objects
    - change speed
    - change direction
    - change range of sensor
    - change latitude
    - change longitude
    - keeping track total number of robots
    - global enable/disable for all robots

## Description
- `class`
    - DriveBot
- `class method`
    - `constructor` assign DEFAULT
        - speed
        - direction
        - sensor_range
    - `control_bot`
        - modify speed
        - modify direction
    - `adjust_sensor`
        - modify sensor
    - `adjust_location`
        - modify latitude
        - modify longitude
    - `global_run`
        - globally enable/disable all robots
## Output
```
>>> python .\script.py
Creating robot # 1
Creating robot # 2
Creating robot # 3

Robot 1:
        Motor Speed: ..........15 ft/s
        Direction: ............50 deg
        Sensor Range: .........20 ft
        Latitude, Longitude: ..(-999999, -999999)
        Robot Engine Status: ..True
Robot 2:
        Motor Speed: ..........35 ft/s
        Direction: ............75 deg
        Sensor Range: .........25 ft
        Latitude, Longitude: ..(-999999, -999999)
        Robot Engine Status: ..True
Robot 3:
        Motor Speed: ..........20 ft/s
        Direction: ............60 deg
        Sensor Range: .........10 ft
        Latitude, Longitude: ..(-999999, -999999)
        Robot Engine Status: ..True
```