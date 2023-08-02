"""
Write a program to log messages at all 5 levels. 

The program should go on and query the log file based on the supplied logging level. 

The program will accept 2 values as input.

The first will be the file name for the log file and the second value will be the logging level to query. 

The message entries for each level should be:

DEBUG – “10:Debug test…”

INFO – “20:Program successful!”

WARNING - “30:Warning, there could be errors…”

ERROR - “40:Program encountered and error!”

CRITICAL – “50:The program has stopped working!”

For example, when the user enters:
log 30

Output should be:
Warning, there could be errors…

"""
import logging

def logMessage(numIn):
    if numIn == "10":
        logging.debug(“10:Debug test…”)
        return("Debug test…")
    
    if numIn == "20":
        logging.info(“20:Program successful!”)
        return("Program successful!")
    
    if numIn == "30":
        logging.warning(“30:Warning, there could be errors…”)
        return("Warning, there could be errors…")
    
    if numIn == "40":
        logging.error(“40:Program encountered and error!”)
        return("Program encountered and error!")
    
    if numIn == "50":
        logging.critical(“50:The program has stopped working!”)
        return("The program has stopped working!")


if __name__ == '__main__':
    logName = str(input())

    charIn = ""
    numIn = ""

    for x in logName:
        if x != " " and x.isdigit() != True:
            charIn = charIn + x
        if x.isdigit() == True:
            numIn = numIn + x

    outputReturn = logMessage(numIn)
    print(outputReturn)
    print()
