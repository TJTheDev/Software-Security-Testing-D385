"""
For this lab you will use unit testing to check a null setting using assertions. Use the commented template code provided to do the following:

Use the assertIsNone() function from Python’s unittest library to verify whether an input value is “None” or “not” using a test case. A Boolean value should be returned by this function based upon the assert condition that the two parameter inputs are received. .

The assertIsNone() function will return true if the input value is equal to "None", and false if it is not. In the multiply_numbers function, test for all cases of a null value. Return the not-null value for each condition with a print statement of the null value.

For example, the output to the console from the source code multiply_numbers(5, None) will be the following output:

y is a null value
5 is not None
"""

# Import the unittest module to create and run test cases
import unittest

# Define a function to multiply two numbers
def multiply_numbers(x, y):
    # If x is None, print a message and return y
    if x is None:
        print("x is a null value")
        return y
    # If y is None, print a message and return x
    elif y is None:
        print("y is a null value")
        return x
    # If both x and y are not None, return their product
    else:
        return x * y   

# Define a test case class to test the multiply_numbers function
class TestForNone(unittest.TestCase):
    def test_when_a_is_null(self): # Test case to check when y is None
        try:
            self.assertIsNone(multiply_numbers(5, None)) # Assert that the result of multiply_numbers(5, None) is None
        except AssertionError as msg:
            print(msg) # If the assertion fails, print the error message

if __name__ == '__main__':
    unittest.main()
