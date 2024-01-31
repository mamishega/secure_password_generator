import secrets
import string

# Secure Password Generator Script

print("Secure Password Generator")
try:
    # Use input() to get user input for password length.
    PASSWORD_LENGTH = int(input("Please enter the length of the password: "))

    # Validate the entered password length to ensure it is a positive integer.
    if PASSWORD_LENGTH <= 0:
        raise ValueError("Invalid input. Please enter a valid positive integer for password length.")

    # Generate a random password using secrets module.
    password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(PASSWORD_LENGTH))

    # Display the generated password.
    print("Generated Password:", password)

except ValueError as e:
    print(e)
    exit(1)
