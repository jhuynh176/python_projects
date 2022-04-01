letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
  key:value
  for key, value
  in zip(letters, points)
}
# Blank tile =  0 point
letter_to_points[' '] = 0
print("Letter and points:\n", letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  # print(point_total)
  return point_total

""" 
Create a dictionary called player_to_words that maps players to a list of the words they have played. 
"""
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
print("\nList of words players have played:")
for key, value in player_to_words.items():
  print(key, "\t-->", value)

player_to_points = {}
string_update = "\t {word} = {point} points\t(Total = {player_points} points)"
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0

    print("\n", player, ":")
    # Counting points for each player
    for word in words:
      point = score_word(word)
      player_points += score_word(word)
      print(string_update.format(
        word = word, 
        point = point, 
        player_points = player_points))

    print("Total points:", player_points)
    # Add player and point to dictionary
    player_to_points[player] = player_points

update_point_totals()

print("\nScoreboard:\n", player_to_points)


def winner():
  highest = max(player_to_points.values())
  winner = {}
  print("\nThe Winners are:")
  for player, point in player_to_points.items():
    if point == highest:
      winner[player] = point
      print("\t",player, "with", point, "points")
winner()
  
