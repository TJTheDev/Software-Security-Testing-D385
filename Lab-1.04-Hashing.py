"""
Write a program that will take as input a string of cities along with their city identification numbers. The city ID, City name pair will be comma separated. Process these cities into a hash table (with 10 slots) using the simple hash function with chaining for handling collision. Assume that there are two-word cities such as South Bend.

For example, if input is:

10 Cincinnati,11 Chicago,12 Boston,20 SouthBend,45 Florence

The output would be:

0 Cincinnati SouthBend

1 Chicago

2 Boston

3

4

5 Florence

6

7

8

9
"""

# Define a simple hash function using modulo operation
def simple_hash_function(city_id, num_slots):
    return city_id % num_slots

# Process the input string of city ID and names into a hash table with chaining
def process_cities(input_str):
    # Split the input string into a list of city ID and name pairs
    city_list = input_str.split(',')

    # Create an empty hash table with 10 slots, represented as a dictionary
    hash_table = {slot: [] for slot in range(10)}

    # Iterate through each city in the city_list
    for city in city_list:
        # Split the city ID and name using the space as the separator
        city_info = city.split()
        city_id = int(city_info[0])
        city_name = " ".join(city_info[1:])

        # Determine the slot index using the simple hash function
        slot = simple_hash_function(city_id, 10)

        # Append the city name to the corresponding slot in the hash table
        hash_table[slot].append(city_name)

    # Return the completed hash table
    return hash_table

# Print the hash table with the cities in each slot
def print_hash_table(hash_table):
    for slot, cities in hash_table.items():
        print(slot, end=' ')
        for city in cities:
            print(city, end=' ')
        print()

if __name__ == "__main__":
    # Get user input for city ID and name pairs (comma-separated)
    input_str = input()

    # Process the input and create the hash table
    hash_table = process_cities(input_str)

    # Print the resulting hash table
    print_hash_table(hash_table)
