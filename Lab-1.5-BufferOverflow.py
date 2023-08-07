""""
Write a program that will take as input, an index to the list [5, 10, 15, 20, 25]. The program should then print the element referenced by the entered index along with the elements that come immediately before and after. Use exception handling to handle out of index references. The program should notify the user when such an exception occurs.

Ex: If the input of the program is:
1

the output of the program is:
5, 10, 15

Ex: If the input of the program is:
4

the output of the program is:
One of the elements is out of bounds

"""

def listChecker(ogElement):
    # Calculate the indices of the elements before and after the specified index
    elementBefore = ogElement - 1
    elementAfter = ogElement + 1

    # Print the elements at the specified index, before, and after
    print(numberedList[elementBefore], numberedList[ogElement], numberedList[elementAfter], end="")
    
    # Return an empty string (not used for any specific purpose)
    return ""
    
if __name__ == '__main__':
    # Define the list of numbers
    numberedList = [5, 10, 15, 20, 25]

    # Get user input for the index
    numIn = int(input())

    # Check if the index is out of bounds
    if numIn > 3:
        print("One of the elements is out of bounds")
    else:
        # Call the listChecker function and print the result
        print(listChecker(numIn))
  
