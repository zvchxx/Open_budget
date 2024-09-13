from queries.for_season import insert_season_query, update_season_query, delete_season_query  



                                                    #Season
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def season_create():
    start_date = input("Enter season start date(YYYY-MM-DD HH:MM:SS): ")
    end_date = input("Enter season end date(YYYY-MM-DD HH:MM:SS): ")
    money = input("Enter season money: ")

    insert_season_query(start_date=start_date, end_date=end_date, is_active=True, money=money,status=True)
    print(f"\nCreated Successfully!") 
    return None


def season_update():
    season_id = int(input("Enter season ID: "))
    start_date = int(input("Enter season start date(YYYY-MM-DD HH:MM:SS): "))
    end_date = int(input("Enter season end date(YYYY-MM-DD HH:MM:SS): "))
    money = input("Enter season money: ")

    update_season_query(season_id=season_id, start_date=start_date, end_date=end_date, is_active=True, money=money, status=True)
    print(f"Update Successfully!") 
    return None


def season_delete():
    season_id = int(input("Enter season ID: "))

    delete_season_query(season_id=season_id)

    print(f"Delete Successfully!")
    return None
    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            #Accepting function
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def accepting_requests_by_id():
    appeal_id = input("Enter appeal ID: ")
    inf = input("Enter appeal information: ")

    pass