import random
# Create a dictionary to store the passwords
password_locker = {}

# Function to generate a random password
def generate_password(length):
    characters = "manish123"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
# Function to add a new password to the locker
def add_password(account, password):
    password_locker[account] = password

# Function to get a password from the locker
def get_password(account):
    return password_locker[account]

# Function to delete a password from the locker
def delete_password(account):
    del password_locker[account]

# Main function
if __name__ == "__main__":
    # Generate a random password
    password = generate_password(8)

    # Add the password to the locker
    add_password("email", password)
    add_password("bank", password)
    add_password("social media", password)

    # Get the password for the "email" account
    print(get_password("email"))

    # Delete the password for the "bank" account
    delete_password("bank")

    # Print the contents of the locker
    print(password_locker)
