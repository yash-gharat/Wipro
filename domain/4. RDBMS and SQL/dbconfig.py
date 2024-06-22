import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        database='fortis',
        user='root',
        password = 'root'

)
print('connection successful')
cursor = connection.cursor()
sql_query = '''select * from login'''
cursor.execute(sql_query)
result = cursor.fetchall()
print(result)



