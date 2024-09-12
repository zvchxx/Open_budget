from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import voice_printer


def create_voices_table_query() -> None:
    """
    Creates a table for storing voices.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS voices (
        id BIGSERIAL PRIMARY KEY,
        vote_id BIGINT REFERENCES votes(id) UNIQUE NOT NULL,
        petition_id BIGINT REFERENCES petitions(id) UNIQUE NOT NULL,
        user_id BIGINIT REFERENCES users(id) UNIQUE NOT NULL
    );
    """)
    return None


def get_voice_from_id_query(voice_id: int) -> DictRow:
    """
    Retrieves a voice from the database by its ID.

    Args:
        voice_id (int): The ID of the voice to retrieve.

    Returns:
        DictRow: The retrieved voice.
    """
    query = f"SELECT * FROM voices WHERE id = %s;"
    params = (voice_id,)
    result = execute_query(query, params, fetch='one')
    return result


def get_voice_from_is_user_id_query(user_id: int) -> DictRow:
    """
    Retrieves a voice from the database by its name.

    Args:
        name (str): The name of the voice to retrieve.

    Returns:
        DictRow: The retrieved voice.
    """
    query = f"SELECT * FROM voices WHERE user_id = %s;"
    params = (user_id,)
    result = execute_query(query, params, fetch='one')
    return result


def insert_voice_query(vote_id: int, petition_id: int, user_id: int) -> None:
    """
    Inserts a new voice into the database.

    Args:
        name (str): The name of the new voice.

    Returns:
        None.
    """
    query = """INSERT INTO voices (vote_id, petition_id, user_id) VALUES (%s, %s, %s);"""
    params = (vote_id, petition_id, user_id,)
    execute_query(query, params)
    return None

