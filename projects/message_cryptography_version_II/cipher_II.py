def welcome_menu():
    print("Welcome to Decode and Encode - Version II:\n")
    print("[1]. Decode\n"\
          "[2]. Encode\n"\
          "[3]. Brute Force Decode --> ( NEW )")

    while(True):
        option = input("Enter your option here: ")
        if option == '1' or option == '2' or option == '3':
            break
        else:
            print("Invalid option. Please retry.\n")
    return option

def prompt_input(option):
    if option == '1' or option == '2':
        message = input("Enter your working message here: ")
        offset = int(input("Enter your offset number here: "))
    elif option == '3':
        message = input("Enter your working message here: ")
        print("Offset: Unknown")
        offset = list(range(1,27))
    return message, offset

def run_cipher(option):
    if option == '1':
        decode_message(message, offset)
    elif option == '2':
        encode_message(message, offset)
    elif option == '3':
        brute_force_decode(message, offset)

def decode_message(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            # Getting the letter index in alphabet
            letter_index = alphabet.find(letter)
            decoded_message +=  alphabet[(letter_index + offset) % 26]
        else:
            decoded_message += letter
    print("\nThis is the decoded message:\n\t-->", decoded_message)

def encode_message(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    encoded_message = ""
    for letter in message:
        if letter in alphabet:
            # Getting the letter index in alphabet
            letter_index = alphabet.find(letter)
            encoded_message +=  alphabet[(letter_index - offset) % 26]
        else:
            encoded_message += letter
    print("\nThis is the encoded message:\n\t-->", encoded_message)

def brute_force_decode(message, offset):
    print(offset)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    for num in offset:
        decoded_message = ""
        for letter in message:
            if letter in alphabet:
                # Getting the letter index in alphabet
                letter_index = alphabet.find(letter)
                decoded_message +=  alphabet[(letter_index + num) % 26]
            else:
                decoded_message += letter
        print("\nOffset", num, ":\n\t-->", decoded_message)

option = welcome_menu()
message, offset = prompt_input(option)
run_cipher(option)