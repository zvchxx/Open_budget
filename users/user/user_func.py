import smtplib
import threading
import random

from log.logs import log_decorator

from queries.for_appeal import increment_total_voices, insert_appeal_query, update_appeal_query, delete_appeal_query  
from queries.for_appeal import search_appeal, get_all_appeals_query, get_appeals_is_active, get_appeal_id

from utils import additions

from utils.printer import appeal_printer, user_printer

from queries.for_user import get_user_id, update_user_query

from queries.for_city import get_city_from_name_query, insert_city_query


                                                 #appeal
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def appeal_create():
    try:
        result = get_appeals_is_active()
        if result == True:
            print("\nYou have appliedm, I will take you to the update section!")
            appeal_update()
        elif result == False:
            user_id = int(input("Enter your ID: "))
            inf = input("Enter appeal information: ")
            print("""
    ID-1:                   ID-2:                   ID-3:
    Andijon viloyati        Buxoro viloyati         Jizzax viloyati
    ID-4:                   ID-5:                   ID-6:
    Qashqadaryo viloyati    Navoiy viloyati         Namangan viloyati
    ID-7:                   ID-8:                   ID-9:
    Samarqand viloyati      Surxondaryo viloyati     Sirdaryo viloyati
    ID-10:                  ID-11:                  ID-12:
    Toshkent shahri         Toshkent viloyati       Farg`ona viloyati
    ID-13:                  ID-14:                  ID-15:
    Xorazm viloyati         Toshkent                Qoraqalpog`iston Respublikasi
    """)
            region_id = input("Enter city ID: ")
            city_name = input("Enter neighborhood name: ")
            insert_city_query(region_id=region_id, name=city_name)

            result = get_city_from_name_query(name=city_name)

            insert_appeal_query(user_id=user_id, city_id=result, is_information=inf)
            print(f"\nCreated Successfully!") 
            result = get_appeal_id(user_id=user_id)
            print(f"\nYour appeal information:")
            for appeal in result:
                appeal_printer(appeal=appeal)
            return None
    except Exception as e:
        return e


@log_decorator
def appeal_update():
    try:
        appeal_id = int(input("Enter appeal ID: "))
        user_id = int(input("Enter your ID: "))
        inf = input("Enter appeal information: ")
        print("""
    ID-1:                   ID-2:                   ID-3:
    Andijon viloyati        Buxoro viloyati         Jizzax viloyati
    ID-4:                   ID-5:                   ID-6:
    Qashqadaryo viloyati    Navoiy viloyati         Namangan viloyati
    ID-7:                   ID-8:                   ID-9:
    Samarqand viloyati      Surxondaryo viloyati     Sirdaryo viloyati
    ID-10:                  ID-11:                  ID-12:
    Toshkent shahri         Toshkent viloyati       Farg`ona viloyati
    ID-13:                  ID-14:                  ID-15:
    Xorazm viloyati         Toshkent                Qoraqalpog`iston Respublikasi
    """)
        region_id = input("Enter city ID: ")
        city_name = input("Enter neighborhood name: ")
        insert_city_query(region_id=region_id, name=city_name)

        result = get_city_from_name_query(name=city_name)

        update_appeal_query(appeal_id=appeal_id, user_id=user_id, city_id=result, is_information=inf)
        print(f"\nCreated Successfully!") 
        result = get_appeal_id(user_id=user_id)
        print(f"\nYour appeal information:")
        for appeal in result:
            appeal_printer(appeal=appeal)
        return None
    except Exception as a :
        print(f"Error: {a}")


@log_decorator
def appeal_delete():
    try:
        appeal_id = int(input("Enter appeal ID: "))

        delete_appeal_query(appeal_id=appeal_id)

        print(f"\nDelete Successfully!")
        return None
    except Exception as a :
        print(f"Error: {a}")

@log_decorator
def show_my_appeal():
    try:
        appeal_id = int(input("Enter your appeal ID: "))
        search_appeal(appeal_id=appeal_id)
        return None
    except Exception as a :
        print(f"Error: {a}")


@log_decorator
def show_all_appeals():
    try:
        get_all_appeals_query()
        return None
    except Exception as a :
        print(f"Error: {a}")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            #My profile
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def update_profile():
    try:
        user_id = int(input("Enter user ID: "))
        email: str = input("Enter your new email: ")
        # Check if the email address is unique
        while not email.endswith(additions.email_details):
            print("\nInvalid email format. Please use one of the following formats: @mail.ru, @gmail.com, @icloud.com")
            email = input("\nRe-Enter new your email: ")

        password: str = input("Enter your new password: ")
        while not password or len(password) < 4:
            print("\nPassword must be at least 4 characters long!")
            password = input("\nRe-Enter your new password: ")

        password_confirmation: str = input("Confirm your new password: ")
        # Check if the password and password confirmation match
        while password!= password_confirmation:
            print("\nPasswords do not match!")
            password_confirmation = input("\nRe-Confirm your new password: ")

        first_name: str = input("Enter your new First Name: ")
        while not first_name:
            print("\nFirst Name is required!")
            first_name = input("\nRe-Enter your new First Name: ")

        last_name: str = input("Enter your new Last Name: ")
        while not last_name:
            print("\nLast Name is required!")
            last_name = input("\nRe-Enter your new Last Name: ")

        update_user_query(user_id=user_id, email=email, password=password, last_name=last_name, first_name=first_name, status=True, )
        print(f"Update Successfully!") 
        result = get_user_id()
        print(f"Your new user profile:\n")
        for user in result:
                user_printer(user=user)
        return None
    except Exception as a :
        print(f"Error: {a}")


@log_decorator
def my_profile():
    try:
        result = get_user_id()
        print(f"\nYour profile:")
        for user in result:
                user_printer(user=user)
        print(
            """
    1. Update 
    2. Quit
    """
        )    
        choice = input("Enter your choice: ")
        if choice == '1':
            update_profile()
        elif choice == '2':
            return None
        else:
            print("Invalid choice. Please try again.")
            return my_profile()
    except Exception as a :
        print(f"Error: {a}")
    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            #My profile
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


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
        print(f"\nFailed {e}")


@log_decorator
def vote_appeal():
    try:
        appeal_id = input("Which appeal will you vote for: ")
        enter_email = input("Enter your email address: ")

        password = str(random.randint(000000, 666666))

        t = threading.Thread(target=send_gmail, args=(enter_email, "Open Budget", password,))
        t.start()

        enter_password = str(input("Enter code: "))
        while enter_password != password:
            print("\nWithout typing the EXIT word, it goes to the menu")
            enter_password = str(input("\nRe-Enter code: "))
            if enter_password == "EXIT" or enter_password == "exit":
                return None

        increment_total_voices(appeal_id=appeal_id)
        print("\nYour vote has been received!")
        return None
    except Exception as a :
        print(f"Error: {a}")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""