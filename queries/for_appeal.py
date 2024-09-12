from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import appeal_printer


def create_appeals_table_query() -> None:
    """
    Creates a table for storing appeals.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS appeals (
        id BIGSERIAL PRIMARY KEY,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        is_active BOOlEAN NOT NULL,
        season_id BIGINT NOT NULL REFERENCES seasons(id),
        total_appeales BIGINT NOT NULL,
        status BOOLEAN DEFAULT FALSE
    );
    """)
    return None


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


def insert_appeal_query(start_date: str, end_date: str, is_active: bool, season_id: int, total_appeals: str, status: bool) -> None:
    """
    Inserts a new appeal into the database.

    Args:
        name (str): The name of the new appeal.

    Returns:
        None.
    """
    query = "INSERT INTO appeals (start_date, end_date, is_active, season_id, total_appeals, status) VALUES (%s, %s, %s, %s, %s, %s);"
    params = (start_date, end_date, is_active, season_id, total_appeals, status,)
    execute_query(query, params)
    return None


def update_appeal_query(appeal_id: int, start_date: str, end_date: str, is_active: bool, season_id: int, total_appeals: str, status: bool) -> None:
    """
    Updates a appeal's name in the database.

    Args:
        appeal_id (int): The ID of the appeal to update.
        name (str): The new name of the appeal.

    Returns:
        None.
    """
    query = "UPDATE appeals SET start_date = %s, end_date = %s, is_active = %s, season_id = %s, total_appeals = %s, status = %s WHERE id = %s;"
    params = (start_date, end_date, is_active, season_id, total_appeals, status, appeal_id,)
    execute_query(query, params)
    return None


def delete_appeal_query(appeal_id: int) -> None:
    """
    Deletes a appeal from the database.

    Args:
        appeal_id (int): The ID of the appeal to delete.

    Returns:
        None.
    """
    query = "Delete appeals WHERE id = %s;"
    params = ( appeal_id,)
    execute_query(query, params)
    return None


def get_all_appeals_query() -> list:
    """
    Retrieves all appeals from the database.

    Returns:
        List[DictRow]: The retrieved appeals.
    """
    query = "SELECT * FROM appeals;"
    result = execute_query(query, fetch='all')
    if result:
        print("appeals:")
        for appeal in result:
           appeal_printer(appeal=appeal)
    else:
        print("No appeals found.")
    return result


def search_appeal(appeal_id: int):
    """
    Search for appeal in the appeal table.
    """
    query = "SELECT * FROM appeal WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + appeal_id + "%",), fetch="all")
    if result:
        print("appeal:")
        for appeal in result:
           appeal_printer(appeal=appeal)
    else:
        print("No appeal found.")
    return None