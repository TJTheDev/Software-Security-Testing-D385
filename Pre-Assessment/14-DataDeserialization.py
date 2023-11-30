"""
To protect against remote code execution, it is important to validate incoming data for deserialization . One way to ensure the integrity of incoming data is to validate it using generated digest keys.

Using the provided template code, complete the function to validate incoming serialized data. For the purpose of this lab, you have access to the generate_key() and deserialize() functions.

Your function should return the result of deserialize() if it passes validation, otherwise it should raise an Exception

If the code is not fixed properly, the output to the console will be:

Error: New key does not match old key
Alternatively, when the code is fixed properly, the output to the console will be:

(Your program produced no output)
"""

from generate_key import generate_key
from deserialize import deserialize 
from serialize import serialize

def safe_deserialize(key, serialized_data):

    new_key = generate_key(serialized_data)
    
    try:
        if key == new_key:
            return deserialize(serialized_data)
        else:
            raise Exception('New key does not match old key')
    except Exception as error:
        print('Error:', error)
        
    return False

# Example usage

grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serialized_data = serialize(grades)
deserialized_data = safe_deserialize(generate_key(serialized_data), serialized_data)
