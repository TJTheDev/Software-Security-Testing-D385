"""

"""

import logging

# Configure the logging settings (e.g., log level and output format)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def logMessage(numIn):
    if numIn == "10":
        logging.debug("10: Debug test…")
        return "Debug test…"
    
    if numIn == "20":
        logging.info("20: Program successful!")
        return "Program successful!"
    
    if numIn == "30":
        logging.warning("30: Warning, there could be errors…")
        return "Warning, there could be errors…"
    
    if numIn == "40":
        logging.error("40: Program encountered an error!")
        return "Program encountered an error!"
    
    if numIn == "50":
        logging.critical("50: The program has stopped working!")
        return "The program has stopped working!"

if __name__ == '__main__':
    logName = input()  # Get user input as a string

    charIn = ""
    numIn = ""

    # Separate characters and digits from the user input
    for x in logName:
        if x != " " and x.isdigit() != True:
            charIn += x
        if x.isdigit() == True:
            numIn += x

    # Call the logMessage function with the numeric part of the input
    outputReturn = logMessage(numIn)
    
    # Print the log message returned by the function
    print(outputReturn)
    print()
  
