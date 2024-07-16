import random

# Ask user if they want a password
user_input = input("Do you want a password? (yes/no): ")

if user_input.lower() == 'yes':
    letters = "ABCDEFGHIJKLMNO"
    digits = "0123456789"
    symbols = "!@#$%^&*()"
    
    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate a password of a specified length
    password_length = 12  # You can set this to any length you prefer
    password = ''.join(random.choice(all_characters) for i in range(password_length))

    print("Your password is:", password)
else:
    print("Okay, no password will be generated.")
