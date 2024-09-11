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

