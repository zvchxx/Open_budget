from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator

from utils.printer import vote_printer


@log_decorator
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
        season_id BIGINT NOT NULL REFERENCES seasons(id),
        is_email VARCHAR(128) NOT NULL REFERENCES users(email),
        status BOOLEAN DEFAULT FALSE
    );
    """)
    return None


@log_decorator
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


@log_decorator
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


@log_decorator
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


@log_decorator
def update_vote_query(vote_id: int, start_date: str, end_date: str, is_active: bool, season_id: int, is_email: str,
                        status: bool) -> None:
    """
    Updates a vote's name in the database.

    Args:
        vote_id (int): The ID of the vote to update.
        name (str): The new name of the vote.

    Returns:
        None.
    """
    query = """UPDATE votes SET start_date = %s, end_date = %s, is_active = %s, season_id = %s, is_email = %s,
                        status = %s WHERE id = %s;"""
    params = (start_date, end_date, is_active, season_id, is_email, status, vote_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_vote_query(vote_id: int) -> None:
    """
    Deletes a vote from the database.

    Args:
        vote_id (int): The ID of the vote to delete.

    Returns:
        None.
    """
    query = "Delete votes WHERE id = %s;"
    params = ( vote_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_votes_query() -> list:
    """
    Retrieves all votes from the database.

    Returns:
        List[DictRow]: The retrieved votes.
    """
    query = "SELECT * FROM votes;"
    result = execute_query(query, fetch='all')
    if result:
        print("votes:")
        for vote in result:
           vote_printer(vote=vote)
    else:
        print("No votes found.")
    return result


@log_decorator
def search_vote(vote_id: int):
    """
    Search for vote in the vote table.
    """
    query = "SELECT * FROM vote WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + vote_id + "%",), fetch="all")
    if result:
        print("vote:")
        for vote in result:
           vote_printer(vote=vote)
    else:
        print("No vote found.")
    return None