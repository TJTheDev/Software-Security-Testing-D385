"""
Nearly everything is done online where users can sign-up using a username and password. Malicious hackers can steal your password and access your bank account or any personal information. Passwords are stored using encryption or hashing. Both methods provide valuable capabilities; however, symmetric encryption is a reversible operation and based on the use of an encryption key. Anyone possessing the key can decrypt an encrypted value to obtain the original value.

The hashing operation is not reversible.

Using a broken or weak cryptographic hash function can leave data vulnerable and should not be used in security related code.

The template code shows a function for hashing passwords, but it is using a weak and insecure hashing algorithm. Fix the code to ensure that the hashing matches the below sample inputs and outputs to prevent tampering. Be sure to analyze each line of code to ensure your hashing algorithm is secure.

Hint: use hex instead of binary.

For example, if the input is:

Password
The output to the console will be the following:

545e50bcc34933b23852a89857e05d6a524b2101e79858d6f65c99a36be4e862
Alternatively, if the input is:

Love3Python
The output to the console will be the following:

c9e1c3bc7cf1f2c1b01296085d57acd66f90921dcc55c08a0bd6744b19aecb8c
"""

import hashlib

def hash_password(pwd):
    # encode password string to bytes
    enc_pwd = pwd.encode()
    
    # call the sha3_256() function returns a hash object
		# call update on the encoded password string
    d = hashlib.sha3_256()
    d.update(enc_pwd)
    
    # generate binary hash of password string in hexidecimal
    hash = d.hexdigest()
    
    return hash
    
if __name__ == '__main__':
    pwd = "Password"
    
    print(hash_password(pwd))
