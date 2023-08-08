"""
The purpose of this lab is to introduce students to the process of creating, accessing, and generating log files using code. Use the template provided in order to write code that outputs log information with the basic configuration of level name and message, based on the information in the template.
 
When you divide a number by zero, write an error message to the log.
 
For Example, the following input:

For Example, if the input is:
9
0
 
The output to the console will be the following:
ERROR: The exception that occurred is: division by zero
 
Alternatively, if the input is:
10
2
 
The output to the console will be the following:
5.0
 
Alternatively, if the input is:
0
20
 
The output to the console will be the following:
0.0
"""
import logging
import sys

# Define a function to handle division by zero error and log it while printing the output to the screen.
def divideByZeroError(dividend, divisor):

    # Configure the logging module to output messages to sys.stdout with a specific format.
    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:
	    # Attempt division to get the quotient.
	    quotient = dividend/divisor
	    print (quotient)
        
    except Exception as e:

	    # If an exception occurs during division, log the error using the logging module, including the exception message (str(e)).
	    logging.error(' The exception that occurred is: ' + str(e))

if __name__ == '__main__': 
	# Get the values for dividend and divisor from user input.
	dividend = int(input())
	divisor = int(input())
	
	# Call the divideByZeroError function with the provided input values to handle any potential division errors.
	divideByZeroError(dividend,divisor)
