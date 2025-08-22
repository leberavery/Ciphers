# Ciphers
# By Avery Leber
# June 19 2025
# Encrypt or decrypt messages using Caesar or Vigenere ciphers.  

class Ciphers:
    def __init__(self, message, direction=1):
        self.message = message
        if direction not in (1, -1):
            raise ValueError('Direction must be 1 (encrypt) or -1 (decrypt).')
        self.direction = direction

class Caesar(Ciphers):
    def caesar_cipher(self, offset):
        if offset <= 0:
            raise ValueError('Offset must be greater than 0.')
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypted_text = ''

        for char in self.message.lower():
            # Append any non-letter character to the message
            if not char.isalpha():
                encrypted_text += char
            else:
                # Find the right character to encode
                index = alphabet.find(char)
                # Define the encrpyred letter
                new_index = (index + offset * self.direction) % len(alphabet)
                encrypted_text += alphabet[new_index]

        action = "Encrypted" if self.direction == 1 else "Decrypted"
        
        return (f'\nPlain Caesar Text: {self.message}'
                f'\nOffset: {offset}'
                f'\n{action} Caesar Text: {encrypted_text}\n')

class Vigenere(Ciphers):
    def vigenere_cipher(self, key):
        if not key.isalpha():
            raise ValueError('Invalid Key. Please only use alphabetic characters.')
        
        key = key.lower()
        key_index = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_message = ''

        for char in self.message.lower():
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
                new_index = (index + offset*self.direction) % len(alphabet)
                final_message += alphabet[new_index]

        action = "Encrypted" if self.direction == 1 else "Decrypted"

        return (f'\nPlain Vigenere Text: {self.message}'
                f'\nKey: {key}'
                f'\n{action} Vigenere Text: {final_message}\n')

# possible code improvements:
# allow for repeating code without restarting
# handle empty input strings
# output results to file
# add other ciphers 
# gui?


