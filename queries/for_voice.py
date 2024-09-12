from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator

from utils.printer import voice_printer


@log_decorator
def create_voices_table_query() -> None:
    """
    Creates a table for storing voices.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS voices (
        id BIGSERIAL PRIMARY KEY,
        vote_id BIGINT NOT NULL REFERENCES votes(id),
        petition_id BIGINT NOT NULL REFERENCES petitions(id),
        user_id BIGINT NOT NULL REFERENCES users(id)
    );
    """)
    return None


@log_decorator
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


@log_decorator
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


@log_decorator
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


@log_decorator
def update_voice_query(voice_id: int, vote_id: int, petition_id: int, user_id: int) -> None:
    """
    Updates a voice's name in the database.

    Args:
        voice_id (int): The ID of the voice to update.
        name (str): The new name of the voice.

    Returns:
        None.
    """
    query = """UPDATE voices SET vote_id = %s, petition_id = %s, user_id = %s WHERE id = %s;"""
    params = (vote_id, petition_id, user_id, voice_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_voice_query(voice_id: int) -> None:
    """
    Deletes a voice from the database.

    Args:
        voice_id (int): The ID of the voice to delete.

    Returns:
        None.
    """
    query = "Delete voices WHERE id = %s;"
    params = ( voice_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_voices_query() -> list:
    """
    Retrieves all voices from the database.

    Returns:
        List[DictRow]: The retrieved voices.
    """
    query = "SELECT * FROM voices;"
    result = execute_query(query, fetch='all')
    if result:
        print("voices:")
        for voice in result:
           voice_printer(voice=voice)
    else:
        print("No voices found.")
    return result


@log_decorator
def search_voice(voice_id: int):
    """
    Search for voice in the voice table.
    """
    query = "SELECT * FROM voice WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + voice_id + "%",), fetch="all")
    if result:
        print("voice:")
        for voice in result:
           voice_printer(voice=voice)
    else:
        print("No voice found.")
    return None