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


def get_region_from_id_query(region_id: int) -> DictRow:
    """
    Retrieves a region from the database by its ID.

    Args:
        region_id (int): The ID of the region to retrieve.

    Returns:
        DictRow: The retrieved region.
    """
    query = f"SELECT * FROM regions WHERE id = %s AND status = %s;"
    params = (region_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_region_from_name_query(name: str) -> DictRow:
    """
    Retrieves a region from the database by its name.

    Args:
        name (str): The name of the region to retrieve.

    Returns:
        DictRow: The retrieved region.
    """
    query = f"SELECT * FROM regions WHERE name = %s AND status = %s;"
    params = (name, True)
    result = execute_query(query, params, fetch='one')
    return result

