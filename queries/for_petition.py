from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import petition_printer


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
        city_id BIGINT REFERENCES citys(id) UNIQUE NOT NULL,
        is_winner BOOLEAN NOT NULL,
        is_accepted BOOLEAN NOT NULL,
        appeal_id BIGINT REFERENCES apeals(id) UNIQUE NOT NULL,
        category_id BIGINT REFERENCES categorys(id) UNIQUE NOT NULL,
        total_voices BIGINT NOT NULL,
        status BOOLEAN NOT NULL,
        user_id BIGINT REFERENCES users(id) UNIQUE NOT NULL,    
    );
    """)
    return None


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
                status = %s, user_id = %s, WHERE id = %s;"""
    params = (title, content, money, city_id, is_winner,
                is_accepted, appeal_id, category_id, total_voices,
                status, user_id, petition_id,)
    execute_query(query, params)
    return None


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

