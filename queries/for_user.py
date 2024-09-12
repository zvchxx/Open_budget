from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator

from utils.printer import user_printer


@log_decorator
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
        created_at TIMESTAMPTZ DEFAULT NOW()
    );
    """)
    return None


@log_decorator
def get_user_from_id_query(user_id: int) -> DictRow:
    """
    Creates a query for retrieving a user by their ID from the database.

    Args:
        user_id (int): The ID of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE id = %s;"
    params = (user_id)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def get_user_from_email_query(email: str) -> DictRow:
    """
    Creates a query for retrieving a user by their email from the database.

    Args:
        email (str): The email address of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE email = %s;"
    params = (email,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def insert_user_query(email: str, password: str, first_name: str, last_name: str) -> None:
    """
    Creates a query for inserting a new user into the database.

    Args:
        email (str): The email address of the user.
        password (str): The password for the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    query = """
    INSERT INTO users (email, password, first_name, last_name)
    VALUES (%s, %s, %s, %s);
    """
    params = (email, password, first_name, last_name,)
    execute_query(query, params)
    return None


@log_decorator
def update_user_query(user_id: int, email: str, password: str, first_name: str, last_name: str) -> None:
    """
    Creates a query for updating a user's information in the database.

    Args:
        user_id (int): The ID of the user.
        email (str): The email address of the user.
        password (str): The password for the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    query = """
    UPDATE users
    SET email = %s, password = %s, first_name = %s, last_name = %s
    WHERE id = %s;
    """
    params = (email, password, first_name, last_name, user_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_user_query(user_id: int) -> None:
    """
    Creates a query for deleting a user from the database.

    Args:
        user_id (int): The ID of the user.
    """
    query = "Delete users WHERE id = %s;"
    params = (user_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_users_query() -> list:
    """
    Creates a query for retrieving all users from the database.

    Returns:
        List[DictRow]: The retrieved users.
    """
    query = "SELECT * FROM users;"
    result = execute_query(query, fetch='all')
    if result:
        print("users:")
        for user in result:
            user_printer(user=user)
    else:
        print("No users found.")
    return None


@log_decorator
def get_users_by_role_query(role_id: int) -> list:
    """
    Creates a query for retrieving users by their role ID from the database.

    Args:
        role_id (int): The ID of the user's role.

    Returns:
        List[DictRow]: The retrieved users.
    """
    query = "SELECT * FROM users WHERE role_id = %s;"
    params = (role_id,)
    result = execute_query(query, params, fetch='all')
    return result


@log_decorator
def search_user(user_id: int):
    """
    Search for user in the user table.
    """
    query = "SELECT * FROM user WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + user_id + "%",), fetch="all")
    if result:
        print("user:")
        for user in result:
           user_printer(user=user)
    else:
        print("No user found.")
    return None