from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_regions_table_query() -> None:
    """
    Creates a table for storing regions.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS regions (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE,
        status BOOLEAN DEFAULT False
    );
    """)
    return None
