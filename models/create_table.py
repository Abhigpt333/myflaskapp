import psycopg2

connection = psycopg2.connect(user="postgres",password="mysecretpassword",host="database",port="5432",dbname="testdb")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real);"
cursor.execute(create_table)

create_user_table = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username text, password text);"
#delete_user_table = "DROP TABLE users"
cursor.execute(create_user_table)


connection.commit()
connection.close()
