import psycopg2

import env


connection = psycopg2.connect(database=env.POSTGRES_DB, user=env.POSTGRES_USER, password=env.POSTGRES_PASSWORD, host="localhost", port=5432)

cursor = connection.cursor()

def log_cursor():
    cursor.execute("SELECT * from products;")

    # Fetch all rows from database
    record = cursor.fetchall()

    return record