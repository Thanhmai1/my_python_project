import mysql.connector
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="animal_db"
    )
    return connection
def save_to_db(animals):
    connection = connect_db()
    cursor = connection.cursor()
    for animal in animals:
        animal_type = type(animal).__name__
        cursor.execute("INSERT INTO animals (name, type) VALUES (%s, %s)",(animal.name, animal_type))
    connection.commit()
    cursor.close()
    connection.close()
    print("Data saved")
