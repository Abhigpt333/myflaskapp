import psycopg2

def find_user_by_username(username):
    connection = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320",database="testdb")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    if result:
        return {"id": result[0],"username": result[1], "password": result[2]}

def find_user_by_id(user_id):
    connection = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320",database="testdb")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id=%s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    if result:
        return {"id": result[0],"username": result[1], "password": result[2]}

def insert_user_by_username(user):
    conn = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320", database="testdb")
    cursor = conn.cursor()
    query = "INSERT INTO users(username,password) VALUES (%s,%s)"
    cursor.execute(query, (user["username"], user["password"]))
    conn.commit()
    conn.close()

def find_item_by_name(name):
    connection = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320",database="testdb")
    cursor = connection.cursor()
    query = "SELECT * FROM items WHERE name=%s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    if result:
        return {"item": {"name": result[0], "price": result[1]}}

#def user_auth(name):
 #   connection = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320", database="testdb")
  #  cursor = connection.cursor()
   # query = "SELECT password from users WHERE username=%s"
 #   cursor.execute(query, (name,))
  #  result = cursor.fetchone()
   # connection.commit()
    #connection.close()
    #return result[0]

def insert_item_by_name(item):
    conn = psycopg2.connect(user="postgres", password="mysecretpassword", host="database", port="54320", database="testdb")
    cursor = conn.cursor()
    query = "INSERT INTO items VALUES (%s, %s)"
    cursor.execute(query, (item["name"], item["price"]))
    conn.commit()
    conn.close()

def update_item(item):

    connection = psycopg2.connect(user="postgres",password="mysecretpassword",host="database",port="54320",database="testdb")
    cursor = connection.cursor()

    query = "UPDATE items SET price=%s WHERE name=%s"
    cursor.execute(query, (item["price"], item["name"]))

    connection.commit()
    connection.close()

def delete(name):
     connection = psycopg2.connect(user="postgres",password="mysecretpassword",host="database",port="54320",database="testdb")
     cursor = connection.cursor()

     query = "DELETE FROM items WHERE name=%s"
     cursor.execute(query, (name,))

     connection.commit()
     connection.close()


def get_all():
    connection = psycopg2.connect(user="postgres",password="mysecretpassword",host="database",port="54320",database="testdb")
    cursor = connection.cursor()

    query = "SELECT * FROM items"

    cursor.execute(query)
    result = cursor.fetchall()
    item = []
    for row in result:
        item.append({"name": row[0], "price": row[1]})

    connection.commit()
    connection.close()
    return item

def get_all_users():
    connection = psycopg2.connect(user="postgres",password="mysecretpassword",host="database",port="54320",database="testdb")
    cursor = connection.cursor()

    query = "SELECT * FROM users"

    cursor.execute(query)
    result = cursor.fetchall()
    item = []
    for row in result:
        item.append({"id": row[0], "username": row[1], "password": row[2]})

    connection.commit()
    connection.close()
    return item