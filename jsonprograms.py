import json

import mysql.connector

mydb_connect = mysql.connector.connect(
    host="localhost", user="root", password="", database="company"
)
cursor = mydb_connect.cursor()

cursor.execute("""
    create table if not exists student_json(
        id int primary key auto_increment,
        details JSON
    )
""")
print("Table created successfully")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
userdata = {"name": name, "marks": marks}
json_data = json.dumps(userdata)

cursor.execute("insert into student_json(details) values(%s)", (json_data,))
mydb_connect.commit()
print("Data inserted successfully")

cursor.execute("select * from student_json")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
mydb_connect.close()
print("Database connection closed")
