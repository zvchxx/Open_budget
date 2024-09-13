from queries.for_appeal import get_accepting_appeals_query, get_all_appeals_admin_query
from utils.printer import appeal_printer

from .admin_func import announce_winners, season_create, season_delete, season_update, accepting_requests_by_id


def admin_menu():
    print("""
1. Season
2. Accepting requests
3. Announcement of winners
4. View results
5. Quit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        season_menu()
        admin_menu()
        return admin_menu()
    elif choice == '2':
        accepting_menu()
        return admin_menu()
    elif choice == '3':
        announce_winners()
        return admin_menu()
    elif choice == '4':
        result = get_all_appeals_admin_query() 
        num = 0
        for appeal in result:
            num += 1
            f"""
            {print(f"{num})")}:
                {appeal_printer(appeal=appeal)}
                """
        return admin_menu()
    elif choice == '5':
        print("\nBacking...")
        return None
    else:
        print("Invalid choice. Please try again.")
        return admin_menu()


def accepting_menu():
    get_accepting_appeals_query()
    print("""""
1. Accepting requests by ID
2. Quit
""")
    choice = input("Enter your choice: ")

    if choice == '1':
        accepting_requests_by_id()
    elif choice == '2':
        admin_menu()
    else:
        print("Invalid choice. Please try again.")
       
    return accepting_menu()


def season_menu():
    print("""\n
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