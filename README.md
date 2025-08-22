# Ciphers
A cipher is a way of encrypting (or disguising) messages in a way that can only be deciphered if the reader has the correct key or code.

This program offers two ciphers:
1. The Caesar Cipher, where every letter of the original message is "shifted" an x number of times down the alphabet. Changing the value of x will change how the text is encrypted.
2. The Vegenere Cipher, where every letter of the original message is encoded with a different Caesar cipher that corresponds to the letter of a secret "key."

This is accomplished by creating a parent class known as Ciphers that accepts a message (self-explanatory) and a direction. The direction determines whether the program should encrypt (direction=1) or decrypt the message (direction = -1). The two child classes, Caesar and Vegenere, inherit these attributes. 

Each child class applies the correct formula for the encryption of their respective cipher and returns the original plaintext message, the offset (Caesar) or key (Vegenere), and the newly encrypted message.
