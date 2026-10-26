import mysql.connector

# establishing the connection
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="company"
)
if mydb.is_connected():
    print("Database connected")

# creating a cursor object
cursor = mydb.cursor()

# creating a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_connection (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(50),
        student_age INT,
        student_place VARCHAR(50)
    )
""")

# truncate the table to avoid duplicate entries
cursor.execute("TRUNCATE TABLE student_connection")
print("Table truncated successfully")

# inserting data into the table
cursor.execute(
    "insert into student_connection values (%s,%s,%s,%s)", (1, "Vesna", 20, "Snezhnaya")
)
mydb.commit()


cursor.execute(
    "insert into student_connection values (%s,%s,%s,%s)",
    (2, "Danica", 20, "Snezhnaya"),
)
mydb.commit()
print("Data inserted successfully")

cursor.execute("update student_connection set student_age=21 where student_id=1")
mydb.commit()
print("Age updated successfully")

# updating using variables-sql injection
updated_name = "Tsaritsa"
updated_age = 2000
updated_place = " Neur Snezhnaya"
query = "update student_connection set student_name=%s,student_age=%s,student_place=%s where student_id=%s"
values = (updated_name, updated_age, updated_place, 1)
cursor.execute(query, values)
mydb.commit()
print("Data updated successfully")

# deleting data from the table
delete_query = "delete from student_connection where student_id=%s"
cursor.execute(delete_query, (1,))
mydb.commit()
print("Data deleted successfully")


cursor.execute("SELECT * FROM student_connection")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
mydb.close()
print("Database connection closed")
