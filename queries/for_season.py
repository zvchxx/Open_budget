from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator

from utils.printer import season_printer


@log_decorator
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
        status BOOLEAN DEFAULT FALSE
    );
    """)
    return None


@log_decorator
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


@log_decorator
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


@log_decorator
def insert_season_query(start_date: str, end_date: str, is_active: bool, status: bool) -> None:
    """
    Inserts a new season into the database.

    Args:
        name (str): The name of the new season.

    Returns:
        None.
    """
    query = "INSERT INTO seasons (start_date, end_date, is_active, status) VALUES (%s, %s, %s, %s);"
    params = (start_date, end_date, is_active, status,)
    execute_query(query, params)
    return None


@log_decorator
def update_season_query(season_id: int, start_date: str, end_date: str, is_active: bool, status: bool) -> None:
    """
    Updates a season's name in the database.

    Args:
        season_id (int): The ID of the season to update.
        name (str): The new name of the season.

    Returns:
        None.
    """
    query = "UPDATE seasons SET start_date = %s, end_date = %s, is_active = %s, status = %s WHERE id = %s;"
    params = (start_date, end_date, is_active, status, season_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_season_query(season_id: int) -> None:
    """
    Deletes a season from the database.

    Args:
        season_id (int): The ID of the season to delete.

    Returns:
        None.
    """
    query = "Delete seasons WHERE id = %s;"
    params = ( season_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_seasons_query() -> list:
    """
    Retrieves all seasons from the database.

    Returns:
        List[DictRow]: The retrieved seasons.
    """
    query = "SELECT * FROM seasons;"
    result = execute_query(query, fetch='all')
    if result:
        print("seasons:")
        for season in result:
           season_printer(season=season)
    else:
        print("No seasons found.")
    return result


@log_decorator
def search_season(season_id: int):
    """
    Search for season in the season table.
    """
    query = "SELECT * FROM season WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + season_id + "%",), fetch="all")
    if result:
        print("season:")
        for season in result:
           season_printer(season=season)
    else:
        print("No season found.")
    return None