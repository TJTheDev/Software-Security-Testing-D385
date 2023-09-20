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
