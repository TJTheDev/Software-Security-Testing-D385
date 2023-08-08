"""
DOS attacks on network traffic are on the rise. In this lab, use AES encryption to ensure your TCP is not vulnerable.

Using the provided template code, fix the encrypt function which should pass the plain_text to be encrypted. Use line 15 in the templated code to encrypt the variable input cipher.

For example, if the input is:

This is a secret message.
The output to the console should be the following:

Enter message: AAAAAAAAAAAAAAAAAAAAEMGL1m8afoCe3ddRA+oFr+O1jtpvSXaU25KjSg/6V6PktYKfb190gdvI108D+gSr8PDN63RTZNPXz9dDRvoSqeXwl59xX2SA39uSDDLhHrm3/JCffRpklt3OklZG5BK55PSE2jJuf5rNnJ5RRuhXufL2kdpoGnqWzc+WRQOnI6L+5sPWbxp2083ZlFAD/Ven8uaQ3ntfOafW1YQCD/pXq7fmhtxuX2PT09mEUQfuEuTD/YrMPFNk09+chEcF+xK+t/iGzG9bcJaQ6J9LFakeubf0w8x5WWWWypyaRxX6Fq3yu7fXdUk3ms2clgIV7BS48uHD0nlJZJLZ2dkkYI9xzJE=
"""

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        counter = self.block_size.to_bytes(self.block_size, "big")
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: counter)
        encrypted_text = cipher.encrypt(plain_text)
        return b64encode(counter + encrypted_text).decode("utf-8")

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

if __name__ == '__main__':

    msg = input("Enter message: ")
    cipher = AESCipher(msg)
    #Test the message size
    msg = msg*10
    
    print(cipher.encrypt(msg))
