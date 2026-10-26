import mysql.connector
from mysql.connector import Error

cursor_obj = None
connect = None

try:
    connect = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="company",
    )
    if connect.is_connected():
        print("Connected to database!")
        cursor_obj = connect.cursor()

        cursor_obj.execute("""
            create table if not exists company_employees(
                emp_id int auto_increment primary key,
                emp_name varchar(50) not null,
                join_date date,
                field_emp varchar(50),
                contact_num bigint unique,
                salary decimal(12,2) default null
            )
        """)

        cursor_obj.execute("truncate table company_employees")

        connect.start_transaction()

        cursor_obj.execute(
            "insert into company_employees(emp_name, join_date, field_emp, contact_num) "
            "values(%s, %s, %s, %s)",
            ("Tony", "2024-05-15", "UI/UX", 9867598762),
        )

        cursor_obj.execute("savepoint sp1")
        print("Savepoint sp1 created.")

        cursor_obj.execute("select * from company_employees")
        rows = cursor_obj.fetchall()
        for row in rows:
            print(row)

        cursor_obj.execute(
            "update company_employees set salary = %s where emp_id = %s",
            (8000.00, 1),
        )

        cursor_obj.execute("savepoint sp2")
        print("Savepoint sp2 created!")

        cursor_obj.execute("select * from company_employees")
        rows = cursor_obj.fetchall()
        for row in rows:
            print(row)

        cursor_obj.execute("ROLLBACK TO SAVEPOINT sp1")
        print("Rolling back to savepoint 1")

        cursor_obj.execute("SELECT * FROM company_employees")
        rows = cursor_obj.fetchall()
        print("Data after rollback to sp1 (salary column exists but no salary data):")
        for row in rows:
            print(row)

        connect.commit()

except Error as e:
    print("Error while connecting database!", e)

finally:
    if cursor_obj:
        cursor_obj.close()
    if connect and connect.is_connected():
        connect.close()
        print("MySQL connection is closed")
