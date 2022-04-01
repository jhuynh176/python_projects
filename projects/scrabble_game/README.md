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