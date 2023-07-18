"""
You are being asked to check that the user input is valid before accepting it. As part of this process, you will validate that the data received is of the expected length.

Using the provided template code, validate that the length of a password meets length requirements. Create a conditional statement that checks if the length of a password input is greater than or equal to 8 characters. Output the correct statement depending on the length of the user's password.

For example, if the input input of appropriate character length is:

12345678
The output to the console will be the following:

Your password is long enough.
Alternatively, if the input of inappropriate character length is:

1234
The output to the console will be the following:

Your password is too short.
"""

#check if the length of the password is at least 8 characters

if __name__ == '__main__': 
        
    password = input()
    
    #write an if / else statement to evaluate passwords length
    if len(password) >= 8:
        print("Your password is long enough.")
    else: 
        print("Your password is too short.")
