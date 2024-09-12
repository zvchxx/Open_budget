from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from log.logs import log_decorator

from utils.printer import city_printer


@log_decorator
def create_citys_table_query() -> None:
    """
    Creates a table for storing citys.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS citys (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE,
        region_id BIGINT NOT NULL REFERENCES regions(id)
    );
    """)
    return None


@log_decorator
def get__city_id_query(city_id: int) -> DictRow:
    """
    Retrieves a city from the database by its ID.

    Args:
        city_id (int): The ID of the city to retrieve.

    Returns:
        DictRow: The retrieved city.
    """
    query = f"SELECT * FROM citys WHERE id = %s;"
    params = (city_id,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def get_city_from_name_query(name: str) -> DictRow:
    """
    Retrieves a city from the database by its name.

    Args:
        name (str): The name of the city to retrieve.

    Returns:
        DictRow: The retrieved city.
    """
    query = f"SELECT * FROM citys WHERE name = %s;"
    params = (name,)
    result = execute_query(query, params, fetch='one')
    return result


@log_decorator
def insert_city_query(name: str, region_id: int) -> None:
    """
    Inserts a new city into the database.

    Args:
        name (str): The name of the new city.

    Returns:
        None.
    """
    query = "INSERT INTO citys (name, region_id) VALUES (%s, %s);"
    params = (name, region_id,)
    execute_query(query, params)
    return None


@log_decorator
def update_city_query(city_id: int, name: str, region_id: int) -> None:
    """
    Updates a city's name in the database.

    Args:
        city_id (int): The ID of the city to update.
        name (str): The new name of the city.

    Returns:
        None.
    """
    query = "UPDATE citys SET name = %s, region_id %s WHERE id = %s;"
    params = (name, region_id, city_id,)
    execute_query(query, params)
    return None


@log_decorator
def delete_city_query(city_id: int) -> None:
    """
    Deletes a city from the database.

    Args:
        city_id (int): The ID of the city to delete.

    Returns:
        None.
    """
    query = "Delete citys WHERE id = %s;"
    params = ( city_id,)
    execute_query(query, params)
    return None


@log_decorator
def get_all_citys_query() -> list:
    """
    Retrieves all citys from the database.

    Returns:
        List[DictRow]: The retrieved citys.
    """
    query = "SELECT * FROM citys;"
    result = execute_query(query, fetch='all')
    if result:
        print("citys:")
        for city in result:
           city_printer(city=city)
    else:
        print("No citys found.")
    return result


@log_decorator
def search_city(city_id: int):
    """
    Search for city in the city table.
    """
    query = "SELECT * FROM city WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + city_id + "%",), fetch="all")
    if result:
        print("city:")
        for city in result:
           city_printer(city=city)
    else:
        print("No city found.")
    return None