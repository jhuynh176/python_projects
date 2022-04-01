# Scrabble

## Introduction
- In this project, 
    - you will process some data from a group of friends playing scrabble
    - you will use dictionaries to organize 
        - `players`, 
        - `words`, 
        - `points`

## Description
- Create two lists:
    - `letters`
    - `points`
- Combine these two into a `dictionary` that would `map` a letter to its point value.
- Using:
    - `list comprehension`
    - `zip`
    - `dictionary`
    - `key`
    - `value`
- Create a function that will:
    - `take` in a word 
    - `return` how many points that word is worth
- Create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
- Create a dictionary called `player_to_words` that maps players to a list of the words they have played. 
- Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.

## Extension
- Create:
    - `play_word()` — a function that would take in a player and a word, and add that word to the list of words they’ve played
    - `update_point_totals()` — turn your nested loops into a function that you can call any time a word is played
    - make your `letter_to_points` dictionary able to `handle lowercase inputs` as well

## Rule
```
# Two Lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary
letter_to_points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
```

## Output
```
Letter and points:
 {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}
 
List of words players have played:
player1 	--> ['BLUE', 'TENNIS', 'EXIT']
wordNerd 	--> ['EARTH', 'EYES', 'MACHINE']
Lexi Con 	--> ['ERASER', 'BELLY', 'HUSKY']
Prof Reader 	--> ['ZAP', 'COMA', 'PERIOD']

 player1 :
	 BLUE = 6 points	(Total = 6 points)
	 TENNIS = 12 points	(Total = 18 points)
	 EXIT = 11 points	(Total = 29 points)
Total points: 29

 wordNerd :
	 EARTH = 8 points	(Total = 8 points)
	 EYES = 7 points	(Total = 15 points)
	 MACHINE = 17 points	(Total = 32 points)
Total points: 32

 Lexi Con :
	 ERASER = 6 points	(Total = 6 points)
	 BELLY = 10 points	(Total = 16 points)
	 HUSKY = 15 points	(Total = 31 points)
Total points: 31

 Prof Reader :
	 ZAP = 14 points	(Total = 14 points)
	 COMA = 8 points	(Total = 22 points)
	 PERIOD = 9 points	(Total = 31 points)
Total points: 31

Scoreboard:
 {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

The Winners are:
	 wordNerd with 32 points
```