from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import vote_printer


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
        season_id BIGINT REFERENCES seasons(id) UNIQUE NOT NULL,
        is_email BIGINIT REFERENCES users(email) UNIQUE NOT NULL
        status BOOLEAN NOT NULL  
    );
    """)
    return None

