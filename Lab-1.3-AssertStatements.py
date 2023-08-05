"""
Instructions
Write a program that will accept four grades and place them in a list. The sum of the 4 grades should be less or equal to 100. Each individual grade should be greater or equal to 0, but less or equal to 100. Include an assert statement that will display a message if any of these conditions are not met.

Ex: If the input of the program is:
25, 10, 15, 25

the output of the program is:
75

Ex: If the input of the program is:
25, 30, 20, 40

the output of the program is:
One of the grades is wrong

Ex: If the input of the program is:
25, 30, -1, 40

the output of the program is:
One of the grades is wrong

"""

"""
Original attempt 6/8 had issue with 101 value
def gradeOut(numList):
    
    listOut = int(numList[0]) + int(numList[1]) + int(numList[2]) + int(numList[3])
    
    if int(max(numList)) > 100:
        return ("All values need to be greater than 0 but less than 100")
    elif listOut > 100:
        return ("One of the grades is wrong, total needs to be less than 100!")
    elif listOut > 100:
        return ("One of the grades is wrong, total needs to be less than 100!")
    else:
        return(listOut)

if __name__ == '__main__':
    userInput = str(input())
    
    numList = []
    numConjure = ""
    errorOut = ""
    
    for x in userInput:
        if x == "-":
            errorOut = "All values need to be greater than 0 but less than 100"
        if x != "," and x != "-":
            if x != " ":
                numConjure = numConjure + x
                # if int(numConjure) > 100 or int(numConjure) < 0:
                #     errorOut = "One of the grades is wrong"
                # else:
                #     numList.append(numConjure)
                #     numConjure = ""
            else:
                numList.append(numConjure)
                numConjure = ""
    numList.append(numConjure)
        
    if errorOut != "":
        print ("All values need to be greater than 0 but less than 100")
    else:
        print(gradeOut(numList))
"""

def gradeOut(numList):
    # Calculate the sum of grades in the numList
    listOut = sum(int(grade) for grade in numList)
    
    # Check if any grade in the numList is greater than 100
    if any(int(grade) > 100 for grade in numList):
        return "All values need to be greater than 0 but less than 100"
    # Check if the total sum of grades exceeds 100
    elif listOut > 100:
        return "One of the grades is wrong, total needs to be less than 100!"
    else:
        return listOut

if __name__ == '__main__':
    # Get user input for grades
    userInput = input()  # No need to convert to string here
    
    # Split the userInput based on spaces and remove commas
    numList = userInput.replace(',', '').split()
    errorOut = ""

    # Loop through each grade in numList
    for grade in numList:
        # Check if the grade is not a valid integer or out of range (0-100)
        if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
            errorOut = "One of the grades is wrong"
            break

    # Check if there was any error in the grades
    if errorOut != "":
        print("All values need to be greater than 0 but less than 100")
    else:
        # Call gradeOut function and print the result
        print(gradeOut(numList))
