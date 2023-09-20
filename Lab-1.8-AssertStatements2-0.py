def gradeOut(numList):
    listOut = sum(int(grade) for grade in numList)
    
    if any(int(grade) > 100 for grade in numList):
        return "All values need to be greater than 0 but less than 100"
    elif listOut > 100:
        return "One of the grades is wrong, total needs to be less than 100!"
    else:
        return listOut

if __name__ == '__main__':
    userInput = input()  # No need to convert to string here
    
    numList = userInput.replace(',', '').split()  # Remove commas and split by spaces
    errorOut = ""

    for grade in numList:
        if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
            errorOut = "One of the grades is wrong"
            break

    if errorOut != "":
        print("All values need to be greater than 0 but less than 100")
    else:
        print(gradeOut(numList))
