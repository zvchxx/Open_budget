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
        season_id BIGINT REFERENCES season(id) UNIQUE NOT NULL,
        total_appeales BIGINT NOT NULL,
        status BOOLEAN NOT NULL
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

