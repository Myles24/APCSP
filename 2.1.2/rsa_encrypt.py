#   a212_rsa_encrypt.py
from sre_compile import isstring
import rsa as rsa


def encrypt():
    
    key = (input("Enter the Encryption Key: " ))
    if key.isdigit():
        pass
    else:
        print("try again")
        encrypt()
    mod_value = int(input("Enter the Modulus: " ))
    plaintext = input("Enter a message to encrypt: ")
    encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
    print("Encrypted Message:", encrypted_msg)

encrypt()



