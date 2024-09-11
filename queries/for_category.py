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


