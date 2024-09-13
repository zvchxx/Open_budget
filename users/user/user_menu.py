from auth.login import logout

from queries.for_season import get_season_from_is_active_query

from queries.for_user import update_users_status_query

from .user_func import appeal_delete, appeal_create, appeal_update, my_profile, show_my_appeal, show_all_appeals, vote_appeal


def user_menu():
    update_users_status_query()
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
        status = get_season_from_is_active_query(is_active=True)
        if True == status:
            appeal_menu()
        else:
            print("\nThe season hasn't started yet!")
        return user_menu()
    elif choice == '2':
        show_my_appeal()
        return user_menu()
    elif choice == '3':
        vote_appeal()
        return user_menu()
    elif choice == '4':
        my_profile()
        return user_menu()
    elif choice == '5':
        show_all_appeals()
        return user_menu()
    elif choice == '6':
        print("Backing...")
        return logout()
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
        return user_menu()
    else:
        print("Invalid choice. Please try again.")
        return appeal_menu()