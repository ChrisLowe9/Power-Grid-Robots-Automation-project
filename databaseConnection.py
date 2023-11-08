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

def read_query(connection, query, param=None):
    # The optional param arg is set as 'None' by default, which I hoped meant
    # that it wouldn't do anything. But even set as 'None', the database query doesn't
    # like it. So I have an if / else so that if the user doesn't specify a param, then
    # we do the cursor.execute without it, and I don't need to worry.

    cursor = connection.cursor()
    if param == None:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
    else:
        try:
            cursor.execute(query, param)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

