# Ciphers
# By Avery Leber
# June 19 2025
# This code accepts user input in encoding and decoding messages, choosing a cipher type, and choosing a custom offset # or key 

# determines whether message is to be encoded or decoded
def user_direction():
    while True:
        try:
            encode_or_decode = input('Would you like to Encode or Decode a message? ')
            if encode_or_decode.lower() == 'encode':
                return 1
            elif encode_or_decode.lower() == 'decode':
                return -1
            else:
                print('Error: Invalid Direction Input')
        except ValueError:
            print('Error: Invalid Direction Input')

# asks user to input message to encode/decode
def user_message(direction):
    while True:
        try:    
            if direction == 1:
                txt = input("Message to Encode: ")
                return txt
            elif direction == -1:
                txt = input("Message to Decode: ")
                return txt
            else: 
                print('Error: Invalid Message Input')
        except ValueError:
            print('Error: Invalid Message Input')

# asks user to input cipher type 
def user_cipher_type():
    while True:
        try:
            cipher_type = input("Encryption Type? (Caesar, Vigenere): ")
            if cipher_type.lower() == 'caesar':
                return 'caesar'
            elif cipher_type.lower() == 'vigenere':
                return 'vigenere'
            else:
                print('Please enter valid cipher type')
        except ValueError:
            print('Invalid Input. Please enter a valid cipher type.')

# Caesar Cipher: asks user to input valid positive offset number
def caesar_offset():
    while True:
        try:
            shift = int(input("Enter Offset Number: "))
            if shift > 0:
                return shift  
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Caesar Cipher: each letter in the original 'text' variable is replaced by another letter some fixed number of positions down the alphabet
def caesar(message, offset, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            encrypted_text += char
        else:
            # Find the right character to encode
            index = alphabet.find(char)
            # Define the encrpyred letter
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]

    action = "Encrypted" if direction == 1 else "Decrypted"

    print(f'\nPlain Caesar Text: {message}')
    print(f'Offset: {offset}')
    print(f'{action} Caesar Text: {encrypted_text}')

# Vigenere Cipher: asks user to input custom key
def vigenere_key():
    while True:
        custom_key = input("Enter Key for Vigenere Cipher: ").lower()
        if custom_key.isalpha():
            return custom_key
        else:
            print('Error: Invalid Key. Please only use alphabetic characters.')

# Vigenere Cipher: each letter in the original 'text' variable is encoded by a different Caesar Cipher, 
# whose increment is determined by the corresponding letter of another text: the key
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    action = "Encrypted" if direction == 1 else "Decrypted"

    print(f'\nPlain Vigenere Text: {message}')
    print(f'Key: {key}')
    print(f'{action} Vigenere Text: {final_message}')

def main():
    direction = user_direction()
    text = user_message(direction)
    type = user_cipher_type()
    if type.lower() == "caesar":
        shift = caesar_offset()
        caesar(text, shift, direction)
    elif type.lower() == "vigenere":
        key = vigenere_key()
        vigenere(text, key, direction)
    
main()

# possible code improvements:
# allow for repeating code without restarting
# handle empty input strings
# output results to file
# add other ciphers 
# gui?
