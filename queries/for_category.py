from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import category_printer


def create_categorys_table_query() -> None:
    """
    Creates a table for storing categorys.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS categorys (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE,
        status BOOLEAN NOT NULL
    );
    """)
    return None


def get_category_from_id_query(category_id: int) -> DictRow:
    """
    Retrieves a category from the database by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.

    Returns:
        DictRow: The retrieved category.
    """
    query = f"SELECT * FROM categorys WHERE id = %s;"
    params = (category_id,)
    result = execute_query(query, params, fetch='one')
    return result


def get_category_from_name_query(name: str) -> DictRow:
    """
    Retrieves a category from the database by its name.

    Args:
        name (str): The name of the category to retrieve.

    Returns:
        DictRow: The retrieved category.
    """
    query = f"SELECT * FROM categorys WHERE name = %s;"
    params = (name,)
    result = execute_query(query, params, fetch='one')
    return result


def insert_category_query(name: str, status: bool) -> None:
    """
    Inserts a new category into the database.

    Args:
        name (str): The name of the new category.

    Returns:
        None.
    """
    query = "INSERT INTO categorys (name, status) VALUES (%s, %s);"
    params = (name, bool,)
    execute_query(query, params)
    return None


def update_category_query(category_id: int, name: str, status: bool) -> None:
    """
    Updates a category's name in the database.

    Args:
        category_id (int): The ID of the category to update.
        name (str): The new name of the category.

    Returns:
        None.
    """
    query = "UPDATE categorys SET name = %s, status = %s WHERE id = %s;"
    params = (name, status, category_id,)
    execute_query(query, params)
    return None


def delete_category_query(category_id: int) -> None:
    """
    Deletes a category from the database.

    Args:
        category_id (int): The ID of the category to delete.

    Returns:
        None.
    """
    query = "Delete categorys WHERE id = %s;"
    params = ( category_id,)
    execute_query(query, params)
    return None

