# 1. Write a python program to create person class  include attributes like name,
# country and date of birth .
# implement a method to get the date of birth of person
# store data in database using DAO design pattern

from db_config import MySQLService

my_sql_service = MySQLService()

connection = my_sql_service.get_mysql_connection()

def create_table(connection):
    cursor = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS persons (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255) NOT NULL,
                date_of_birth DATE NOT NULL
            )'''
    cursor.execute(query)
    connection.commit()
    cursor.close()

def insert_person(connection, person):
    cursor = connection.cursor()
    query = 'INSERT INTO persons (name, country, date_of_birth) VALUES (%s, %s, %s)'
    cursor.execute(query, person)
    connection.commit()
    cursor.close()

def get_all_persons(connection):
    cursor = connection.cursor()
    query = 'SELECT * FROM persons'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()

def get_person_by_name(connection,name):
    cursor = connection.cursor()
    query = 'SELECT * FROM persons WHERE name = %s'
    cursor.execute(query,(name,))
    result = cursor.fetchone()
    print(result)
    cursor.close()

def close_connection(connection):
    connection.close()

# Create the table
create_table(connection)

# Insert a person
# person = ("Sara", "India", "1997-07-21")
# insert_person(connection, person)

# gwt all persons
get_all_persons(connection)
# get_person_by_name(connection, "Sara")



# Close the connection
close_connection(connection)
