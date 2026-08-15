
import sys


USERS = {
    "nada": "nada123",
    "student": "pass123",
    "user": "password"
}

def validate(username, password, users =USERS):
    """
    Validate username and password against credentials database.
    Case-insensitive username check, exact password match.
    """

    username_clean = username.strip().lower()
    for user, pwd in users.items():
        if user.lower() == username_clean and pwd == password:
            return True
    return False


def login(n_attempts, users=USERS ):
    """
    Prompt user for login credentials up to max_attempts times.
    Returns True if login succeeds, exits program if all attempts fail.
    """
    attempts_left = n_attempts
    while attempts_left > 0:
        print(f"\n Attempt {n_attempts - attempts_left + 1} of {n_attempts}")
        user_name = input('User name: ')
        pass_word = input('Password: ')
        
        if validate(user_name, pass_word, USERS):
            print(f"\nLogin Successful! Welcome, {user_name}.")
            input("\nPress Enter to continue to Main Menu...")
            return True
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Invalid username or password!. {attempts_left} attempt(s) remaining.")
            else:
                print("\nMaximum login attempts exceeded!")
                sys.exit(0)
    return False
