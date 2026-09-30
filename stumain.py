import json
import os
import pickle

print("------ STUDENT RECORD MANAGEMENT SYSTEM ------")
print("1. Add Student")
print("2. View Students")
print("3. Save as JSON")
print("4. Save as Pickle")
print("5. Exit")

if not os.path.exists("student_records"):
    os.mkdir("student_records")
os.chdir("student_records")

file = open("students.txt", "w")
file.write("Jophin,Class9,85,Present\n")
file.close()

with open("attendance.txt", "w") as f:
    f.write("Jophin,Present\n")

print("Student Added Successfully")

try:
    file = open("students.txt", "r+")
    print("File Name:")
    print(file.name)
    print("File Mode:")
    print(file.mode)
    print("File Closed Status:")
    print(file.closed)

    file.readline()
    print("Current File Pointer Position:")
    print(file.tell())
    file.close()

    print("Directory Contents:")
    print(sorted(os.listdir(), reverse=True))
    os.chdir("..")

    student = {
        "name": "Jophin",
        "class": "Class9",
        "marks": 85,
        "attendance": "Present",
    }

    with open("students.json", "w") as f:
        json.dump(student, f)
    print("JSON File Created Successfully")

    with open("students.pkl", "wb") as f:
        pickle.dump(student, f)
    print("Pickle File Created Successfully")

    with open("students.pkl", "rb") as f:
        pickle.load(f)
    print("Student Records Loaded Successfully")

except FileNotFoundError:
    print("File not found")
finally:
    print("Operation completed")
