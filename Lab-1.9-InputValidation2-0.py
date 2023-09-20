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

    # Calculate the age in hours
    age_in_hours = age_in_days * 24
    return f"{age_in_days}"

if __name__ == '__main__':
    current_date_str = "2022-12-19"

    # Get user input for the date of birth
    birth_date_str = input()

    try:
        # Call the function to calculate the age in hours and print the result
        age_in_hours_result = calculate_age_in_hours(birth_date_str, current_date_str)
        if age_in_hours_result[0] == "I":
            print(age_in_hours_result)
        else:
            print(age_in_hours_result,"")
    except ValueError:
        print("Incorrect date format, please try again!")
