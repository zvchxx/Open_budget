from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator
from utils.printer import petition_printer



@log_decorator
def create_petitions_table_query() -> None:
    """
    Creates a table for storing petitions.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS petitions (
        id BIGSERIAL PRIMARY KEY,
        title VARCHAR(256) NOT NULL,
        content VARCHAR(256) NOT NULL,
        money BIGINT NOT NULL,
        city_id BIGINT NOT NULL REFERENCES citys(id),
        is_winner BOOLEAN NOT NULL,
        is_accepted BOOLEAN NOT NULL,
        appeal_id BIGINT NOT NULL REFERENCES appeals(id),
        category_id BIGINT NOT NULL REFERENCES categorys(id),
        total_voices BIGINT NOT NULL,
        status BOOLEAN DEFAULT FALSE,
        user_id BIGINT NOT NULL REFERENCES users(id)
    );
    """)
    return None


@log_decorator
def get_petition_from_id_query(petition_id: int) -> DictRow:
    """
    Retrieves a petition from the database by its ID.

    Args:
        petition_id (int): The ID of the petition to retrieve.

    Returns:
        DictRow: The retrieved petition.
    """
    query = f"SELECT * FROM petitions WHERE id = %s;"
    params = (petition_id,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def get_petition_from_is_active_query(is_active: bool) -> DictRow:
    """
    Retrieves a petition from the database by its name.

    Args:
        name (str): The name of the petition to retrieve.

    Returns:
        DictRow: The retrieved petition.
    """
    query = f"SELECT * FROM petitions WHERE is_active = %s;"
    params = (is_active,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def insert_petition_query(title: str, content: str, money: str, city_id: int, is_winner: bool,
                        is_accepted: bool, appeal_id: int, category_id: int, total_voices: str,
                        status: bool, user_id: int) -> None:
    """
    Inserts a new petition into the database.

    Args:
        name (str): The name of the new petition.

    Returns:
        None.
    """
    query = """INSERT INTO petitions (title, content, money, city_id, is_winner,
                        is_accepted, appeal_id, category_id, total_voices,
                        status, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    params = (title, content, money, city_id, is_winner,
                is_accepted, appeal_id, category_id, total_voices,
                status, user_id,)
    execute_query(query, params)
    return None


@log_decorator
def update_petition_query(petition_id: int, title: str, content: str, money: str, city_id: int, is_winner: bool,
                        is_accepted: bool, appeal_id: int, category_id: int, total_voices: str,
                        status: bool, user_id: int) -> None:
    """
    Updates a petition's name in the database.

    Args:
        petition_id (int): The ID of the petition to update.
        name (str): The new name of the petition.

    Returns:
        None.
    """
    query = """UPDATE petitions SET title = %s, content = %s, money = %s, city_id = %s, is_winner = %s,
                is_accepted = %s, appeal_id = %s, category_id = %s, total_voices = %s,
                status = %s, user_id = %s WHERE id = %s;"""
    params = (title, content, money, city_id, is_winner,
                is_accepted, appeal_id, category_id, total_voices,
                status, user_id, petition_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_petition_query(petition_id: int) -> None:
    """
    Deletes a petition from the database.

    Args:
        petition_id (int): The ID of the petition to delete.

    Returns:
        None.
    """
    query = "Delete petitions WHERE id = %s;"
    params = ( petition_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_petitions_query() -> list:
    """
    Retrieves all petitions from the database.

    Returns:
        List[DictRow]: The retrieved petitions.
    """
    query = "SELECT * FROM petitions;"
    result = execute_query(query, fetch='all')
    if result:
        print("petitions:")
        for petition in result:
           petition_printer(petition=petition)
    else:
        print("No petitions found.")
    return result


@log_decorator
def search_petition(petition_id: int):
    """
    Search for petition in the petition table.
    """
    query = "SELECT * FROM petition WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + petition_id + "%",), fetch="all")
    if result:
        print("petition:")
        for petition in result:
           petition_printer(petition=petition)
    else:
        print("No petition found.")
    return None