from queries.for_running import if_not_used

from auth.login import login

from auth.register import register

from log.logs import log_settings


def after_login(email: str, status: str):
    """
    Function to handle the after-login actions.
    """
    if status == "admin":
        print("Welcome Admin!")

    elif status == "user":
        print("Welcome User!")


def auth_menu():
    print("""
1. Register
2. Login            admin login&password = admin
3. Quit
""")
    choice = input("Enter your choice: ")

    if choice == '1':
        email = register()
        return auth_menu()
    elif choice == '2':
        data = login()
        if not data:
            return auth_menu()
        email, status = data
        after_login(email=email, status=status)
    elif choice == '3':
        print("Exiting...")
        return None

    else:
        print("Invalid choice. Please try again.")
    return auth_menu()


if __name__ == "__main__":
    if_not_used()
    auth_menu()
    log_settings()