import psycopg2


connection = psycopg2.connect(database="telegram-workout-bot", user="postgres", password="postgres", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from products;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)