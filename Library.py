# Creates a function that checks for the quality of the user's password
def ContainsCharacters(password):
    score = 0
    minLength = 8
    
    # Creates 'lists' of characters that will be checked for in the password
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    specialChars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Checks if the password is at last 8 characters long
    if(len(password) >= minLength):
        score  += 1
    
    # Check for character presence and update the score
    for list in [upperCase, lowerCase, digits, specialChars]:
        if any(char in password for char in list):
            score += 1
    
    # Ensures that the user does not use specific passwords that would be banned in most applications
    if("password".upper() in password or '1234' in password or ' ' in password):
        score = 0
    return score