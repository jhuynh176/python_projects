import csv
import json


with open('passwords.csv') as password_file:
  compromised_users = []
  print("Opening \"password.csv\" file.\n")
  password_csv = csv.DictReader(password_file)

  print("Reading file.")
  for password_row in password_csv:
    print(password_row)
    compromised_users.append(password_row['Username'])

# print(compromised_users)
with open('compromised_users.txt', 'w') as compromised_user_file:
  print("\nRetrieving compromised username.")
  for user in compromised_users:
    print("\t", user)
    compromised_user_file.write(user + '\n')

with open('boss_message.json', 'w') as boss_message:
  print("\nSending message in \"boss_message.json\" file.")
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

  print("Message:\t", boss_message_dict)

with open('new_passwords.csv', 'w') as new_password_obj:
  sig = """
\t _  _     ___   __  ____             
\t/ )( \   / __) /  \(_  _)            
\t) \/ (  ( (_ \(  O ) )(              
\t\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
\t __ _  _  _  __    __                
\t(  ( \/ )( \(  )  (  )               
\t/    /) \/ (/ (_/\/ (_/\             
\t\_)__)\____/\____/\____/
"""
# print(sig)
  new_password_obj.write(sig)
  print("\nOverwriting the compromised \"password.csv\" file.")
  print(sig)

print("\nClosing all opened files.")