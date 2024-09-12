from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import appeal_printer

from log.logs import log_decorator


@log_decorator
def create_appeals_table_query() -> None:
    """
    Creates a table for storing appeals.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS appeals (
        id BIGSERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id),
        is_active BOOlEAN NOT NULL,
        is_information VARCHAR(256) NOT NULL,
        status BOOLEAN DEFAULT FALSE
    );
    """)
    return None


@log_decorator
def get_appeal_from_id_query(appeal_id: int) -> DictRow:
    """
    Retrieves a appeal from the database by its ID.

    Args:
        appeal_id (int): The ID of the appeal to retrieve.

    Returns:
        DictRow: The retrieved appeal.
    """
    query = f"SELECT * FROM appeals WHERE id = %s;"
    params = (appeal_id,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def get_appeal_from_is_active_query(is_active: bool) -> DictRow:
    """
    Retrieves a appeal from the database by its name.

    Args:
        name (str): The name of the appeal to retrieve.

    Returns:
        DictRow: The retrieved appeal.
    """
    query = f"SELECT * FROM appeals WHERE is_active = %s;"
    params = (is_active,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def insert_appeal_query(is_active: bool, user_id: int, is_information: str, status: bool) -> None:
    """
    Inserts a new appeal into the database.

    Args:
        name (str): The name of the new appeal.

    Returns:
        None.
    """
    query = "INSERT INTO appeals (user_id, is_active, is_information, status) VALUES (%s, %s, %s, %s);"
    params = (user_id,  is_active, is_information, status,)
    execute_query(query, params)
    return None


@log_decorator
def update_appeal_query(appeal_id: int, is_active: bool, user_id: int, is_information: str, status: bool) -> None:
    """
    Updates a appeal's name in the database.

    Args:
        appeal_id (int): The ID of the appeal to update.
        name (str): The new name of the appeal.

    Returns:
        None.
    """
    query = "UPDATE appeals SET is_active = %s, user_id = %s, is_information = %s, status = %s WHERE id = %s;"
    params = (is_active, user_id, is_information, status, appeal_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_appeal_query(appeal_id: int) -> None:
    """
    Deletes a appeal from the database.

    Args:
        appeal_id (int): The ID of the appeal to delete.

    """
    query = "DELETE FROM appeals WHERE id = %s;"
    params = ( appeal_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_appeals_query() -> list:
    """
    Retrieves all appeals from the database.

    Returns:
        List[DictRow]: The retrieved appeals.
    """
    query = "SELECT * FROM appeals;"
    result = execute_query(query, fetch='all')
    if result:
        print("Appeals:")
        for appeal in result:
           appeal_printer(appeal=appeal)
    else:
        print("No appeals found.")
    return result


def get_appeals_is_active():
    query = "SELECT is_active FROM appeals WHERE is_active = True LIMIT 1;"
    result = execute_query(query, fetch='one')
    
    active_status = False

    if result is not None:
        active_status = True
    
    return active_status


def get_appeal_id(user_id: int):
    query = "SELECT * FROM appeals WHERE user_id = user_id;"
    params = (user_id,) 

    result = execute_query(query, params=params, fetch='all')

    return result


@log_decorator
def search_appeal(appeal_id: int):
    """
    Search for appeal in the appeal table.
    """
    query = "SELECT * FROM appeals WHERE id = %s;"
    params = (appeal_id,)
    result = execute_query(query, params=params, fetch="all")
    if result:
        print("\nAppeals:")
        for appeal in result:
           appeal_printer(appeal=appeal)
    else:
        print("No appeal found.")
    return None