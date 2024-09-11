from psycopg2.extras import DictRow

from database_config.db_settings import execute_query
from utils.printer import petition_printer


def create_petitions_table_query() -> None:
    """
    Creates a table for storing petitions.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS petitions (
        id BIGSERIAL PRIMARY KEY,
        title VARCHAR(256) NOT NULL,
        content VARCHAR(256) NOT NULL,
        money BIGINT NOT NULL,
        city_id BIGINT REFERENCES citys(id) UNIQUE NOT NULL,
        is_winner BOOLEAN NOT NULL,
        is_accepted BOOLEAN NOT NULL,
        appeal_id BIGINT REFERENCES apeals(id) UNIQUE NOT NULL,
        category_id BIGINT REFERENCES categorys(id) UNIQUE NOT NULL,
        total_voices BIGINT NOT NULL,
        status BOOLEAN NOT NULL,
        user_id BIGINT REFERENCES users(id) UNIQUE NOT NULL,    
    );
    """)
    return None

