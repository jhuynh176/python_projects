def welcome_menu():
    print("Welcome to Decode and Encode - Version I:\n")
    print("[1]. Decode\n"\
          "[2]. Encode\n")

    while(True):
        option = input("Enter your option here: ")
        if option == '1' or option == '2':
            break
        else:
            print("Invalid option. Please retry.\n")
    return option

def prompt_input():
    message = input("Enter your working message here: ")
    offset = input("Enter your offset number here: ")
    return message, int(offset)

def run_cipher(option):
    if option == '1':
        decode_message(message, offset)
    elif option == '2':
        encode_message(message, offset)

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


option = welcome_menu()
message, offset = prompt_input()
run_cipher(option)