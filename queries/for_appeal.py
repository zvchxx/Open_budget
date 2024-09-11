from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import appeal_printer


def create_appeals_table_query() -> None:
    """
    Creates a table for storing appeals.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS appeals (
        id BIGSERIAL PRIMARY KEY,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        is_active BOOlEAN NOT NULL,
        season_id BIGINT REFERENCES season(id) UNIQUE NOT NULL,
        total_appeales BIGINT NOT NULL,
        status BOOLEAN NOT NULL
    );
    """)
    return None

