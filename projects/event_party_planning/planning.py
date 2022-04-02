def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("ERROR - Gamer is missing critical information.")

def build_daily_frequency_table():
    dict = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    return dict

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        # Each gamer has 2 keys: "name", "availability"
        # We want to count "availability"
        for day in gamer["availability"]:
#             print(day)
            available_frequency[day] += 1
    return available_frequency

def find_best_night(availability_table):
    # return key with the highest value
    most_availability_night = ""
    most_availability_number = max(availability_table.values())
    for day in availability_table.keys():
        if most_availability_number == availability_table[day]:
#             print(day)
            most_availability_night = day
    print("Gamers are most available in:", most_availability_night + ", with", most_availability_number, "people")
    return most_availability_night

def available_on_night(gamers_list, day):
    gamers_availability = [
        gamer
        for gamer in gamers_list
        if day in gamer['availability']
    ]
    
    print("List of gamers available on", day, "are:")
    for gamer in gamers_availability:
        print("\t", gamer)
        
    return gamers_availability

form_email = \
"""
Hi {name},

The Gamers's Club is happy to host "{game_title}" night and wishes you will attend. 
Come by on {day} and have a blast!

Happy Gaming,
Gamer's Club
"""

def send_email(gamers_who_can_attend, day, game_title):
    # gamer is a dictionary key = 'name', 'availability'
    for gamer in gamers_who_can_attend:
        print("__________________________________________")
        print(form_email.format(name = gamer['name'], 
                                day = day, 
                                game_title = game_title))
        print("==========================================")

# Gamer list
gamers_list = []

# Add gamers
print("\n>>> Calling add_gamer()")
add_gamer({"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}, gamers_list)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers_list)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers_list)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers_list)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers_list)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers_list)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers_list)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers_list)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers_list)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers_list)

count = 0
for gamer in gamers_list:
    count += 1
    print("\tGamer", count,  ":\t", gamer)

# First night
# ===========================================================================
print("\n>>> Calling build_daily_frequency_table()")
print("\n>>> Calling count_availability()")
count_availability = build_daily_frequency_table()
print("Frequency Table:\n\t", calculate_availability(gamers_list, count_availability))
# print(count_availability)

print("\n>>> Calling find_best_night()")
game_night = find_best_night(count_availability)
print("Gamer night will be celebrated on -->", game_night)

attending_game_night = available_on_night(gamers_list, game_night)

send_email(attending_game_night, game_night, "Elden Ring")
#===========================================================================

# Secondary night 
#===========================================================================
unable_to_attend_best_night = [
    gamer
    for gamer in gamers_list
    if game_night not in gamer['availability']
]

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers_list, second_night)
send_email(available_second_game_night, second_night, "Elden Ring")
#===========================================================================
