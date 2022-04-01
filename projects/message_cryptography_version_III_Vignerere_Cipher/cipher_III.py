from string import punctuation


def welcome_menu():
    print("--------------------------------------------------------------------\n")
    print("|            Welcome to Decode and Encode - Version III            |\n")
    print("--------------------------------------------------------------------\n")
    print("------------------------- Security Level I -------------------------\n")
    print("[1]. Caesar's Cipher - Decoder\n")
    print("[2]. Caesar's Cipher - Encoder\n")
    print("[3]. Caesar's Cipher - Decoder - Brute Force\n")
    print("------------------------- Security Level II ------------------------\n")
    print("[4]. Vigenère Cipher - Decoder\n")
    print("[5]. Vigenère Cipher - Encoder\n")
    print("--------------------------------------------------------------------\n")
    while(True):
        option = input("Enter your option here: ")
        if option == '1' or option == '2' or option == '3' or option == '4' or option == '5':
            break
        else:
            print("Invalid option. Please retry.\n")
    return option

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = ".,?'! "

def run_option(option):
    if option == '1' or option == '2':
        message = input("Enter your working message here: ")
        key = int(input("Enter your offset number here: "))
    elif option == '3':
        message = input("Enter your working message here: ")
        print("Offset: Unknown")
        key = list(range(1,27))
    elif option == '4' or option == '5':
        message = input("Enter your working message here: ")
        key = input("Enter your keyword here: ")
    return message, key

def run_cipher(option):
    if option == '1':
        caesar_decoder(message, key)
    elif option == '2':
        caesar_encoder(message, key)
    elif option == '3':
        caesar_decoder_brute_force(message, key)
    elif option == '4':
        vigenere_decoder(message, key)
    elif option == '5':
        vigenere_encoder(message, key)

def caesar_decoder(message, offset):
    decoded_message = ""
    for letter in message:
        if letter in lower:
            # Getting the letter index in alphabet
            letter_index = lower.find(letter)
            decoded_message +=  lower[(letter_index + offset) % 26]
        elif letter in upper:
            # Getting the letter index in alphabet
            letter_index = upper.find(letter)
            decoded_message +=  upper[(letter_index + offset) % 26]
        else:
            decoded_message += letter
    print("\nThis is the decoded message:\n\t-->", decoded_message)
    return decoded_message

def caesar_encoder(message, offset):
    encoded_message = ""
    for letter in message:
        if letter in lower:
            # Getting the letter index in alphabet
            letter_index = lower.find(letter)
            encoded_message +=  lower[(letter_index - offset) % 26]
        elif letter in upper:
            # Getting the letter index in alphabet
            letter_index = upper.find(letter)
            encoded_message +=  upper[(letter_index - offset) % 26]
        else:
            encoded_message += letter
    print("\nThis is the encoded message:\n\t-->", encoded_message)
    return encoded_message

def caesar_decoder_brute_force(message, nums):
    for offset in nums:
        decoded_message = ""
        for letter in message:
            if letter in lower:
                # Getting the letter index in alphabet
                letter_index = lower.find(letter)
                decoded_message +=  lower[(letter_index + offset) % 26]
            elif letter in upper:
                # Getting the letter index in alphabet
                letter_index = upper.find(letter)
                decoded_message +=  upper[(letter_index + offset) % 26]
            else:
                decoded_message += letter
        print("\nOffset", offset, ":\n\t-->", decoded_message)
    return decoded_message

def vigenere_decoder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)

    decoded_message = ''
    for i in range(0,len(message)):    
        if message[i] in lower:
            ln = lower.find(message[i]) - lower.find(keyword_final[i])
            decoded_message += lower[ln % 26]
        elif message[i] in upper:
            ln = upper.find(message[i]) - upper.find(keyword_final[i])
            decoded_message += upper[ln % 26]
        else:
            decoded_message += message[i]
    print(decoded_message)
    return decoded_message

# message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
# keyword = "friends"

# print(vigenere_decoder(message, keyword))

def vigenere_encoder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    encoded_message = ''
    for i in range(0,len(message)):
        if message[i] in lower:
            ln = lower.find(message[i]) + lower.find(keyword_final[i])
            encoded_message += lower[ln % 26]
        elif message[i] in upper:
            ln = upper.find(message[i]) + upper.find(keyword_final[i])
            encoded_message += upper[ln % 26]
        else:
            encoded_message += message[i]
    print(encoded_message)
    return encoded_message

# message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
# keyword = "besties"

# print(vigenere_coder(message_for_v,keyword))
# print(vigenere_decoder(vigenere_coder(message_for_v, keyword), keyword))

option = welcome_menu()
message, key = run_option(option)
run_cipher(option)