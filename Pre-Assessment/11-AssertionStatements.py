"""
Assertions can be an excellent tool if you're looking for a way to increase the effectiveness of your debugging and testing processes. In the following lab, you will demonstrate the basics of using assert statements, including how to write logical statements and when to use assertion statements in your code.

Using the templated code provided, write an assertion statement where noted in the template code. The assertion statement needs to determine whether an integer input is below freezing using the phrase: "Colder than zero degrees Celsius!".

For example if the input is
-5

The output to the console for your assertion statement will be the following:
Colder than zero degrees Celsius!

If the input is greater than zero degrees Celsius (note: this code is already provided):
5

The output to the console in Fahrenheit will be the following:
41
"""

# Define a function to convert temperature from Celsius to Fahrenheit
def CelciusToFahrenheit(Temperature):

    # Insert an assert statement to check if the temperature is greater than 0
    # If the temperature is not greater than 0, an AssertionError will be raised with the specified message
    assert Temperature > 1, "Colder than zero degrees Celsius!"

    
    # Convert the int of Celsius to Fahrenheit and return the result
    return ((Temperature*9)/5)+32

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    
    # Get user input for the temperature in Celsius
    Temperature = int(input())

    try:
        # Call the CelciusToFahrenheit function with the user-provided temperature
        # If the temperature is colder than zero, an AssertionError will be raised and caught in the except block
        print(CelciusToFahrenheit(Temperature))

    # If an AssertionError occurs, print the error message specified in the assert statement
    except AssertionError as msg:
        print(msg)
