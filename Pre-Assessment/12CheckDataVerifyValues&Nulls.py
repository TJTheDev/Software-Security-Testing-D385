"""
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
