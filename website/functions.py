import re

def is_valid_password(password):
    # Check if the password contains at least one number, one special character, and is at least 8 characters long
    if len(password) >= 8 and \
       re.search(r'\d', password) and \
       re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return True
    return False