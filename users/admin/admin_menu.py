from queries.for_appeal import get_all_appeals_query

from .admin_func import season_create, season_delete, season_update

def admin_menu():
    print("""
1. Season
2. Accepting requests
3. Announcement of winners
4. View results live
5. Quit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        season_menu()
        return admin_menu()
    elif choice == '2':
        accepting_menu()
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print("Backing...")
        return None
    else:
        print("Invalid choice. Please try again.")

    return admin_menu()


def accepting_menu():
    get_all_appeals_query()
    print("""""
1. Accepting requests by ID
2. Quit
""")
    choice = input("Enter your choice: ")

    if choice == '1':
        pass
    elif choice == '2':
        pass
    else:
        print("Invalid choice. Please try again.")
       
    return accepting_menu()


def season_menu():
    print("""\nWelcome to season menu:
1. Create season
2. Update season
3. Delete season
4. Quit
""")
    choice = input("Enter your choice: ")

    if choice == '1':
        season_create()
    elif choice == '2':
        season_update()
    elif choice == '3':
        season_delete()
    elif choice == '4':
        print("Backing...")
        return admin_menu
    else:
        print("Invalid choice. Please try again.")

    return season_menu()