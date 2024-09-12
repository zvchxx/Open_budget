from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import vote_printer


def create_votes_table_query() -> None:
    """
    Creates a table for storing votes.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS votes (
        id BIGSERIAL PRIMARY KEY,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        is_active BOOlEAN NOT NULL,
        season_id BIGINT REFERENCES seasons(id) UNIQUE NOT NULL,
        is_email BIGINIT REFERENCES users(email) UNIQUE NOT NULL
        status BOOLEAN NOT NULL  
    );
    """)
    return None


def get_vote_from_id_query(vote_id: int) -> DictRow:
    """
    Retrieves a vote from the database by its ID.

    Args:
        vote_id (int): The ID of the vote to retrieve.

    Returns:
        DictRow: The retrieved vote.
    """
    query = f"SELECT * FROM votes WHERE id = %s;"
    params = (vote_id,)
    result = execute_query(query, params, fetch='one')
    return result


def get_vote_from_is_active_query(is_active: bool) -> DictRow:
    """
    Retrieves a vote from the database by its name.

    Args:
        name (str): The name of the vote to retrieve.

    Returns:
        DictRow: The retrieved vote.
    """
    query = f"SELECT * FROM votes WHERE is_active = %s;"
    params = (is_active,)
    result = execute_query(query, params, fetch='one')
    return result


def insert_vote_query(start_date: str, end_date: str, is_active: bool, season_id: int, is_email: str,
                        status: bool) -> None:
    """
    Inserts a new vote into the database.

    Args:
        name (str): The name of the new vote.

    Returns:
        None.
    """
    query = """INSERT INTO votes (start_date, end_date, is_active, season_id, is_email,
                        status) VALUES (%s, %s, %s, %s, %s, %s);"""
    params = (start_date, end_date, is_active, season_id, is_email, status,)
    execute_query(query, params)
    return None
