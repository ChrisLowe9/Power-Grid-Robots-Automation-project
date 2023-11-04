import pyodbc
from pyodbc import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pyodbc.connect(
            driver= "MySQL ODBC 8.2 ANSI Driver",
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

