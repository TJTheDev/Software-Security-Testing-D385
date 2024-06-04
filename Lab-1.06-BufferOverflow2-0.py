"""
Write a program that will take as input, an index to the list [5, 10, 15, 20, 25]. 
The program should then print the element referenced by the entered index along with the elements that come immediately before and after. 
Use exception handling to handle out of index references. The program should notify the user when such an exception occurs.
Ex: If the input of the program is:
2

the output of the program is:
10, 15, 20

Ex: If the input of the program is:
0

the output of the program is:
One of the elements is out of bounds

"""

# Define a list of integers
theList = [5, 10, 15, 20, 25]

# Initialize global variables
fail = False  # Indicates whether an exception occurred
checker0 = int  # Placeholder for the value at checker - 1
checker1 = int  # Placeholder for the value at checker
checker2 = int  # Placeholder for the value at checker + 1

# Define a function to check elements at a given index
def checkerApp(checker):
    global checker0, checker1, checker2, fail  # Use global variables
    
    try:
        # Attempt to access list elements
        checker0 = theList[checker - 1]  # Get the element at checker - 1
        checker1 = theList[checker]      # Get the element at checker
        checker2 = theList[checker + 1]  # Get the element at checker + 1
    except IndexError:
        # Handle the case where the index is out of bounds
        print("One of the elements is out of bounds")
        fail = True  # Set fail to True if an exception occurs

if __name__ == '__main__':
    # Get user input for the index to check
    checker = int(input())
    
    # Call the checkerApp function to check the elements
    checkerApp(checker)
    
    # Check if fail is False (i.e., no exceptions occurred)
    if not fail:
        # Print the values at checker - 1, checker, and checker + 1
        print(checker0, checker1, checker2)
