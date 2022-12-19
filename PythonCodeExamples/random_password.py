import string
import random

# Set the length of the password
length = 16

# Set the characters that can be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = "".join(random.choices(characters, k=length))

# Print the password
print(password)
