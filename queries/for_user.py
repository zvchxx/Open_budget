from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


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
        role_id INT REFERENCES user_role(id) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
    );
    """)
    return None

