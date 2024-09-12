from .admin_func import season_create, season_delete, season_update

def admin_menu(email: str):
    print("""
1. Season
2. Accepting requests
3. Announcement of winners
4. All statistics
5. View results live
6. Quit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        season_menu()
        pass

    elif choice == '2':
        # remove_manager(email)
        pass

    elif choice == '3':
        # show_manager(email)
        pass

    elif choice == '4':
        # edit_manager(email)
        pass
    elif choice == '6':
        print("Backing...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return admin_menu(email)


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
        pass

    elif choice == '2':
        season_update()
        pass

    elif choice == '3':
        season_delete()
        pass
    elif choice == '6':
        print("Backing...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return admin_menu()