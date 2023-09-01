import random
import string

def generate_random_string(length):
    # Define the character set from which the random string will be generated
    characters = string.ascii_letters + string.digits  # You can add more characters if needed

    # Generate the random string by sampling characters
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string