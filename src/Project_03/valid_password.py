# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# ○ At least 1 letter between [a-z]
# ○ At least 1 number between [0-9]
# ○ At least 1 letter between [A-Z]
# ○ At least 1 character from [$#@]
# ○ Minimum length of transaction password: 6
# ○ Maximum length of transaction password: 12
# Example - input_password =asqwr1234@1,aF145#,2w3E *,2We3345
# Output = asqwr1234@1

import re


def valid_password(password):
    # Checking the length of the password
    if len(password) < 6 or len(password) > 12:
        return False

    # Checking at-least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Checking at-least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Checking at-least one digit
    if not re.search(r"[0-9]", password):
        return False

    # Checking at-least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if valid_password(password):
        print("Valid Password")
    else:
        print("Invalid Password:", password)
        print("Registration failed. Your password must meet the following criteria:")
        print("- At least 1 letter between [a-z]")
        print("- At least 1 letter between [A-Z]")
        print("- At least 1 number between [0-9]")
        print("- At least 1 character from [$#@]")
        print("- Minimum length of password: 6")
        print("- Maximum length of password: 12")


if __name__ == "__main__":
    register_user()

