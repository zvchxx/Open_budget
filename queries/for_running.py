import os

from database_config.db_settings import execute_query

from .for_user import create_users_table_query
from .for_season import create_seasons_table_query
from .for_appeal import create_appeals_table_query
from .for_city import create_citys_table_query
from .for_region import create_regions_table_query
from .for_category import create_categorys_table_query
from .for_petition import create_petitions_table_query
from .for_voice import create_voices_table_query
from .for_vote import create_votes_table_query


def create_is_used_table_query() -> None:
    """
    Creates a new table for tracking whether the application is already run.
    """
    query = """
        CREATE TABLE IF NOT EXISTS is_used (
            id BIGSERIAL PRIMARY KEY,
            is_used BOOLEAN DEFAULT FALSE
        );
    """
    execute_query(query)
    return None


def insert_is_used_query():
    """
    Inserts a new record into the is_used table.
    """
    query = """
        SELECT * FROM is_used
        ORDER BY id DESC
        LIMIT 1;
        """
    data = execute_query(query, fetch="one")
    if data is None:
        query = "INSERT INTO is_used (is_used) VALUES (False);"
        execute_query(query)
    return None


def update_is_used_query():
    """
    Updates the is_used column in the is_used table.
    """
    query = "UPDATE is_used SET is_used = TRUE;"
    execute_query(query)
    return None


def is_used():
    query = """
    SELECT * FROM is_used
    ORDER BY id DESC
    LIMIT 1;
    """
    data = execute_query(query, fetch="one")
    return data['is_used'] is True


def before_run() -> None:
    """
    Creates all required tables before running the application.
    """
    create_users_table_query()
    create_seasons_table_query()
    create_appeals_table_query()
    create_categorys_table_query()
    create_regions_table_query()
    create_citys_table_query()
    create_votes_table_query()
    create_petitions_table_query()
    create_voices_table_query()

    return None


def if_not_used():
    path = os.path.join(os.path.dirname(__file__),)
    create_is_used_table_query()
    insert_is_used_query()
    if not is_used():
        before_run()

        with open(f"{path}/inserter_for_region.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)
        update_is_used_query()

    return None