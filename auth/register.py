import random
import smtplib
import threading

from queries.for_user import get_user_id, insert_user_query

from utils import additions

from log.logs import log_decorator

from utils.printer import user_printer


smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "abubakrrahmatullayev1001@gmail.com"
smtp_password = "etsk hbbi kuym flhe"


@log_decorator
def send_gmail(to_user, subject, message):
    n_message = f"Subjet: {subject}\n\nPassword: {message}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, n_message)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


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

    rendom_password = str(random.randint(000000, 666666))

    t = threading.Thread(target=send_gmail, args=(email, "Open Budget", rendom_password,))
    t.start()

    enter_password = str(input("Enter code: "))
    while enter_password != rendom_password:
        print("Without typing the EXIT word, it goes to the menu")
        enter_password = str(input("Re-Enter code: "))
        if enter_password == "EXIT" or enter_password == "exit":
            print("\nNot registered!")
            return None
        
    # Create a new user in the database
    insert_user_query(email=email, password=password, last_name=last_name, first_name=first_name, status=True)
    print("Congratulations!!!")
    result = get_user_id()
    print(f"{first_name} {last_name} You Registered Successfully to OpenBudget!")
    print(f"Your information:\n")
    for user in result:
        user_printer(user=user)
    return email