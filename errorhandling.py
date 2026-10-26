import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost", user="root", password="", database="company"
    )
    cursor = connection.cursor()
    cursor.execute("select * from student_connection")
    for row in cursor.fetchall():
        print(row)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    except NameError:
        pass
