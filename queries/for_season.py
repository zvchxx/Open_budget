from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import season_printer


def create_seasons_table_query() -> None:
    """
    Creates a table for storing seasons.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS seasons (
        id BIGSERIAL PRIMARY KEY,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        is_active BOOlEAN NOT NULL,
        status BOOLEAN NOT NULL
    );
    """)
    return None

