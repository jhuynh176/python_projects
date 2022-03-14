"""
This program will gives the customer a fortune based on their questions.

Description:
1. Ask customer for their name.
2. Ask customer for fortune question.
3. Output.
"""

import random 

# Asking customer for name
name = input("What is your name? - ")
question = input("What is your question today? - ")

#Answer will be generated randomly
# import random
# generate random number from 1 - 9 using random.randint(1, 9)

answer = ""

#Print divider
print("")

random_number = random.randint(1, 9)
#print (random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

#Checking for empty question
# if yes, print Error
# if no,  continue
if question == "":
  print("Error: The question is empty.")
else:
  #Checking for empty customer name
  if name == "":
    print ("Question: " + question)
  else:
    print (name + " asks: " + question)
  print ("Magic 8-Ball's answer: " + answer)

