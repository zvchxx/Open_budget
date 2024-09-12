from queries.for_user import get_user_id, insert_user_query

from utils import additions

from log.logs import log_decorator

from utils.printer import user_printer


@log_decorator  
def register():
    """
    Handles the registration process for a new user.
    """
    email: str = input("Enter your email: ")
    # Check if the email address is unique
    while not email.endswith(additions.email_details):
        print("Invalid email format. Please use one of the following formats: @mail.ru, @gmail.com, @icloud.com")
        email = input("Re-Enter your email: ")

    password: str = input("Enter your password: ")
    while not password or len(password) < 4:
        print("Password must be at least 4 characters long!")
        password = input("Re-Enter your password: ")

    password_confirmation: str = input("Confirm your password: ")
    # Check if the password and password confirmation match
    while password!= password_confirmation:
        print("Passwords do not match!")
        password_confirmation = input("Re-Confirm your password: ")

    first_name: str = input("Enter your First Name: ")
    while not first_name:
        print("First Name is required!")
        first_name = input("Re-Enter your First Name: ")

    last_name: str = input("Enter your Last Name: ")
    while not last_name:
        print("Last Name is required!")
        last_name = input("Re-Enter your Last Name: ")


    # Create a new user in the database
    insert_user_query(email=email, password=password, last_name=last_name, first_name=first_name, status=True)
    print("Congratulations!!!")
    result = get_user_id()
    print(f"{first_name} {last_name} You Registered Successfully to OpenBudget!")
    print(f"Your information:\n")
    for user in result:
        user_printer(user=user)
    return email