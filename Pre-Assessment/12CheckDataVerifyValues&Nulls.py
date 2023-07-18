"""
Question
External data quality can affect downstream systems, reporting, and metrics and cause vulnerabilities in our systems. Using the templated code provided, write one method to check if a string is not null and a separate method to check if a string contains all numbers.

Your first variable will be a string and contain a simple sentence, such as "I like dogs." Your second variable will be an integer and will contain a few numbers, such as 12345.

Complete the functions in the code template.

For example, if the variables in the templated code are:
I like dogs.
12345

The output to the console will be the following:
True
True

Alternatively, if the variable values in the template code are changed to:
None
12345

The output to the console will be the following:
False
True

Alternatively, if the variable values in the template code are changed to:
None
"I love dogs"

The output to the console will be the following:
False
False

"""
"""
OG Example Template
# verify we only have digits

def check_numeric_value(wg_int):
    
        #return true if numeric value is an integer, else return false.  
        #Hint: use isinstance function

# verify if the string is null

def check_null_string (wg_string):
    
    # check if wg_string is not null return true else return false
       
if __name__ == '__main__':  
    
    wg_string = "I like dogs." # use keyword None to test
    wg_int = 12345
    
    print(check_null_string (wg_string))
    print(check_numeric_value(wg_int))
"""

"""
Internet Answer
# verify we only have digits
def check_numeric_value(wg_int):

    #return true if numeric value is an integer, else return false.  
    # Check if the input wg_int is a string (since the input is taken as a string)
    if type(wg_int) == str:
        try:
            # Attempt to convert the string to an integer using the int() function
            cast_int = int(wg_int)
            
            # If the conversion is successful, return True, indicating that it is a numeric value and an integer
            return(isinstance(wg_int, int))

        except Exception as e:
            # If an exception occurs during conversion (e.g., due to non-numeric characters in the string), return False
            return False
            
        else:
            # If the input is not a string, return False, as it cannot be a numeric value and an integer
            return(isinstance(wg_int, int))

# verify if the string is null (i.e., contains some non-empty content)
def check_null_string (wg_string):
    
    # Check if the input wg_string is not null (non-empty)
    # If the string is not null (contains some content), return True, indicating that it is not null
    if wg_string:
        return True
    else:
        # If the string is null (empty), return False
        return False
       
# Check if the script is being run directly (not imported as a module)      
if __name__ == '__main__':  
    
    # Prompt the user to input a string and store it in wg_string
    wg_string = input() # use keyword None to test
    
    # Prompt the user to input a numeric value as a string and store it in wg_int    
    wg_int = input()
    
    # Call the check_null_string function with the input string and print the result   
    print(check_null_string (wg_string))
    
    # Call the check_numeric_value function with the input numeric value as a string and print the result    
    print(check_numeric_value(wg_int))
"""

"""
CHAT GPT
# Function to check if the input string is not null (i.e., contains some content)
def check_not_null_string(wg_string):
    # Check if the input wg_string is not null (non-empty)
    # If the string is not null (contains some content), return True, otherwise return False
    if wg_string:
        return True
    else:
        return False

# Function to check if the input string contains all numeric characters
def check_all_numbers(wg_string):
    # Loop through each character in the input string
    for char in wg_string:
        # Check if the character is not a numeric digit (0-9)
        if not char.isdigit():
            return False
    # If all characters are numeric digits, return True
    return True

if __name__ == '__main__':
    # Prompt the user to input a string and store it in wg_string
    wg_string = input()  # e.g., "I like dogs."

    # Prompt the user to input a string containing numbers and store it in wg_numbers
    wg_numbers = input()  # e.g., "12345"

    # Call the check_not_null_string function with the input string and print the result
    print(check_not_null_string(wg_string))

    # Call the check_all_numbers function with the input string containing numbers and print the result
    print(check_all_numbers(wg_numbers))
"""
