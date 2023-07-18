"""
You are being asked to validate that a numeric input is within a pre-defined range.

Using the provided template code, create an input validation check to ensure an input value is within the range of values from 1 to 10, inclusive. Use the range() function to check the input variable's value against the defined range. The code should output a message of "The number input is in the range from 1 and 10." or "The number input is not in the range from 1 and 10." depending on the numeric value of the variable.

For example, if the input within range is:

8
The output to the console will be the following:

The number input is in the range from 1 and 10.
Alternatively, if the input out of range is:

15
The output to the console will be the following:

The number input is not in the range from 1 and 10.
"""

#check if the input range is between 1 and 10 for the range validation check
if __name__ == '__main__': 
        
    r = range(1,10)
    
    num = int(input())
    
    # create conditional statement for range check here
    if num in r:
        print("The number input is in the range from 1 and 10.")
    else:
        print("The number input is not in the range from 1 and 10.")
