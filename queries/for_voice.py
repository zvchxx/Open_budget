from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import voice_printer


def create_voices_table_query() -> None:
    """
    Creates a table for storing voices.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS voices (
        id BIGSERIAL PRIMARY KEY,
        vote_id BIGINT REFERENCES votes(id) UNIQUE NOT NULL,
        petition_id BIGINT REFERENCES petitions(id) UNIQUE NOT NULL,
        user_id BIGINIT REFERENCES users(id) UNIQUE NOT NULL
    );
    """)
    return None

