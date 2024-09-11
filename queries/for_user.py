from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_users_table_query() -> None:
    """
    Creates a query for creating a table for storing users.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS users (
        id BIGSERIAL PRIMARY KEY,
        first_name VARCHAR(64) NOT NULL,
        last_name VARCHAR(64) NOT NULL,
        email VARCHAR(64) NOT NULL UNIQUE,
        password VARCHAR(64) NOT NULL,
        role_id INT REFERENCES user_role(id) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
    );
    """)
    return None


def get_user_from_id_query(user_id: int) -> DictRow:
    """
    Creates a query for retrieving a user by their ID from the database.

    Args:
        user_id (int): The ID of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_user_from_email_query(email: str) -> DictRow:
    """
    Creates a query for retrieving a user by their email from the database.

    Args:
        email (str): The email address of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE email = %s AND status = %s;"
    params = (email, True)
    result = execute_query(query, params, fetch='one')
    return result
