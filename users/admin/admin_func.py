import threading
import smtplib

from log.logs import log_decorator

from queries.for_season import insert_season_query, update_season_query, delete_season_query  

from queries.for_appeal import get_user_email_from_appeal, update_appeal_accept_query, get_top_appeals_by_total_voices

from utils.printer import appeal_printer


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


smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "abubakrrahmatullayev1001@gmail.com"
smtp_password = "etsk hbbi kuym flhe"


@log_decorator
def send_gmail(to_user, subject, message):
    n_message = f"Subjet: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, n_message)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


def accepting_requests_by_id():
    appeal_id = input("Enter appeal ID: ")

    user_subject = "Open Budget"

    message = "Your application has been accepted and you can collect votes!"
    
    result = get_user_email_from_appeal(appeal_id=appeal_id)
    update_appeal_accept_query(appeal_id=appeal_id, is_accepted=True) 

    t = threading.Thread(target=send_gmail, args=(result, user_subject, message,))
    t.start()     

    print("\nAccepting requests\n")

    return None


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                        #Announcement of winners
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def announce_winners():
    result = get_top_appeals_by_total_voices()

    num = 0
    for winner in result:
        num += 1
        f"""
        {print(f"{num})")}:
            {appeal_printer(winner)}
            """
    return None