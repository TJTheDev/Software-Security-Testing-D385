"""
Assume that the current date is 2022-12-19. Write a program that will request the user's date of birth and calculate their age in days.
The program must validate that the entered date is in the correct date format (yyyy-mm-dd).
The program must also validate that the date of birth is not in the future(again assume a current date of 2022-12-19) 

nor way too much in the past than that of the oldest person alive (assume this is Lucile Randon born in 1904-02-11). 

Only when the date of birth entered meets all of these criteria should the age in hours be printed.

Ex: If the input of the program is:

1976-10-28
the output of the program is:

16853 hours.
Ex: If the input of the program is:

2098-01-01
the output of the program is:

Incorrect date, your birthday cannot be in the future!
Ex: If the input of the program is:

1900-01-01
the output of the program is:

Incorrect date, you cannot be older than Lucile Randon!
Ex: If the input of the program is: 1900/01/01

the output of the program is:
Incorrect date format, please try again!

"""

from datetime import datetime, timedelta

def calculate_age_in_hours(birth_date_str, current_date_str):
    # Convert the date strings to datetime objects
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")

    # Define the oldest person alive's birth date (Lucile Randon)
    oldest_person_birth_date = datetime(1904, 2, 11)

    # Validate that the birth date is not in the future
    if birth_date > current_date:
        return "Incorrect date, your birthday cannot be in the future!"

    # Validate that the birth date is not too far in the past
    if birth_date < oldest_person_birth_date:
        return "Incorrect date, you cannot be older than Lucile Randon!"

    # Calculate the age in days
    age_in_days = (current_date - birth_date).days
    return f"{age_in_days} hours."

if __name__ == '__main__':
    current_date_str = "2022-12-19"

    # Get user input for the date of birth
    birth_date_str = input()

    try:
        # Call the function to calculate the age in hours and print the result
        age_in_hours_result = calculate_age_in_hours(birth_date_str, current_date_str)
        print(age_in_hours_result)
    except ValueError:
        print("Incorrect date format, please try again!")
