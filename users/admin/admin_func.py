from queries.for_season import insert_season_query, update_season_query, delete_season_query     



                                                    #Season
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def season_create():
    start_date = "Enter season start date(YYYY-MM-DD HH:MM:SS): "
    end_date = "Enter season end date(YYYY-MM-DD HH:MM:SS): "

    insert_season_query(start_date=start_date, end_date=end_date, is_active=True, status=True)
    print(f"\nCreated Successfully!") 
    return None


def season_update():
    season_id = int(input("Enter season ID: "))
    start_date = int(input("Enter season start date(YYYY-MM-DD HH:MM:SS): "))
    end_date = int(input("Enter season end date(YYYY-MM-DD HH:MM:SS): "))

    update_season_query(season_id=season_id, start_date=start_date, end_date=end_date, is_active=True, status=True)
    print(f"Update Successfully!") 
    return None


def season_delete():
    season_id = int(input("Enter season ID: "))

    delete_season_query(season_id=season_id)

    print(f"Delete Successfully!")
    return None
    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""