from auth.login import logout

from .user_func import appeal_delete, appeal_create, appeal_update, my_profile, show_my_appeal, show_all_appeals


def user_menu():
    print("""
1. Send a appeal
2. My appeal
3. Vote
4. My profile
5. All appeal
6. Quit
""") 
    choice = input("Enter your choice: ")

    if choice == '1':
        appeal_menu()
        return user_menu()
    elif choice == '2':
        show_my_appeal()
        return user_menu()
    elif choice == '3':
        pass
    elif choice == '4':
        my_profile()
        return user_menu()
    elif choice == '5':
        show_all_appeals()
        return user_menu()
    elif choice == '6':
        print("Backing...")
        logout()
    else:
        print("Invalid choice. Please try again.")
    return user_menu()


def appeal_menu():
    print("""
    1. Send a appeal
    2. Delete a appeal
    3. Update a appeal
    4. Quit
""")    
    choice = input("Enter your choice: ")

    if choice == '1':
        appeal_create()
        return appeal_menu()
    elif choice == '2':
        appeal_delete()
        return appeal_menu()
    elif choice == '3':
        appeal_update()
        return appeal_menu()
    elif choice == '4':
        print("Backing...")
        user_menu()
    else:
        print("Invalid choice. Please try again.")
    return appeal_menu()