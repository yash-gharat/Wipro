from db_resource.mysql_connect import MySQLService

# Create an instance of MySQLService
my_sql_service = MySQLService()

# Get the MySQL connection
connection = my_sql_service.get_mysql_connection()

def create_product(connection, product_name, price):
    cursor = connection.cursor()
    query = "INSERT INTO products (product_name, price) VALUES (%s, %s)"
    cursor.execute(query, (product_name, price))
    connection.commit()
    cursor.close()

def read_products(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()

def update_product(connection, product_id, product_name, price):
    cursor = connection.cursor()
    query = "UPDATE products SET product_name = %s, price = %s WHERE product_id = %s"
    cursor.execute(query, (product_name, price, product_id))
    connection.commit()
    cursor.close()

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    cursor.close()
    connection.commit()

# Close the connection after operations are done
def close_connection(connection):
    connection.close()


# create_product(connection, "Hp", 45999)
# create_product(connection, "Asus", 55999)
# create_product(connection, "Dell", 35999)
# create_product(connection, "Acer", 65999)
# create_product(connection, "Gigabyte", 75999)
# read_products(connection)
#
# update_product(connection, 1, "Updated Product", 100)
# read_products(connection)
#
# delete_product(connection, 3)
read_products(connection)

# Close  connection
close_connection(connection)
