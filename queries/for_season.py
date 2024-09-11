from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import season_printer


def create_seasons_table_query() -> None:
    """
    Creates a table for storing seasons.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS seasons (
        id BIGSERIAL PRIMARY KEY,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        is_active BOOlEAN NOT NULL,
        status BOOLEAN NOT NULL
    );
    """)
    return None


def get_season_from_id_query(season_id: int) -> DictRow:
    """
    Retrieves a season from the database by its ID.

    Args:
        season_id (int): The ID of the season to retrieve.

    Returns:
        DictRow: The retrieved season.
    """
    query = f"SELECT * FROM seasons WHERE id = %s;"
    params = (season_id,)
    result = execute_query(query, params, fetch='one')
    return result


def get_season_from_is_active_query(is_active: bool) -> DictRow:
    """
    Retrieves a season from the database by its name.

    Args:
        name (str): The name of the season to retrieve.

    Returns:
        DictRow: The retrieved season.
    """
    query = f"SELECT * FROM seasons WHERE is_active = %s;"
    params = (is_active,)
    result = execute_query(query, params, fetch='one')
    return result

