from queries.for_user import get_user_from_email_query

from log.logs import log_decorator


@log_decorator
def login():
    """
    Handles the login process for a user.
    """
    email: str = input("Enter your email address: ")
    password: str = input("Enter your password: ")

    if email == "admin" and password == "admin":
        print("Login successful as Admin!")
        return "admin", "admin"


    user_data = get_user_from_email_query(email)
    if user_data is None:
        print("Invalid email address. Please try again.")
        return None


    if user_data['password'] != password:
        print("Invalid password. Please try again.")
        return None

    return user_data['email'], "user"