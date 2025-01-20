import bcrypt

def hash_password(password):
    """Hashes a password using bcrypt and returns the hashed password."""
    # Encode the password into bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt for added security
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

def main():
    # Get user input for the password
    password_input = input("Please type in the password you want to hash: ")

    # Validate the password input
    if not password_input:
        print("Error: Password cannot be empty. Please enter a valid password.")
        return

    # Hash the password and display the result
    hashed_password = hash_password(password_input)
    print('Here is your newly hashed password:\n', hashed_password.decode('utf-8'))

if __name__ == "__main__":
    main()
