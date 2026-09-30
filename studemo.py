import json
import os
import pickle

if not os.path.exists("demo_files"):
    os.mkdir("demo_files")
os.chdir("demo_files")
for name in os.listdir():
    os.remove(name)

print("---- x mode, write, writelines ----")
file = open("marks.txt", "x")
file.write("Jophin,85\n")
file.writelines(["John,90\n", "Acer,78\n"])
file.close()

print("---- append mode ----")
file = open("attendance.txt", "w")
file.write("Jophin,Present\n")
file.close()
file = open("attendance.txt", "a")
file.write("John,Absent\n")
file.close()
file = open("attendance.txt", "r")
print(file.read())
file.close()

print("---- read, readline, readlines ----")
file = open("marks.txt", "r")
print(file.read())
file.seek(0)
print(file.readline())
print(file.readlines())
file.close()

print("---- seek and tell ----")
file = open("marks.txt", "r")
print(file.tell())
file.seek(11)
print(file.tell())
print(file.readline())
file.close()

print("---- r+ mode ----")
file = open("marks.txt", "r+")
file.seek(0, 2)
file.write("Ben,88\n")
file.seek(0)
print(file.read())
file.close()

print("---- with statement ----")
with open("marks.txt", "rt") as file:
    print(file.name)
    print(file.mode)
    print(file.closed)
print(file.closed)

print("---- exceptions ----")
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Operation completed")

try:
    file = open("marks.txt", "z")
except ValueError:
    print("Invalid file mode")

file = open("locked.txt", "w")
file.close()
os.chmod("locked.txt", 0o000)
try:
    file = open("locked.txt", "w")
    file.close()
except PermissionError:
    print("Permission denied")
os.chmod("locked.txt", 0o666)

print("---- binary file ----")
file = open("photo.bin", "wb")
file.write(bytes([137, 80, 78, 71, 1, 2, 3]))
file.close()
file = open("photo.bin", "rb")
print(file.read())
file.close()

print("---- report, results, backup ----")
file = open("report.txt", "w")
file.write("Student Report\nJophin - Marks 85 - Present\n")
file.close()
os.rename("report.txt", "student_report.txt")

file = open("exam_results.txt", "w")
file.write("Jophin,Pass\nJohn,Pass\n")
file.close()

old = open("marks.txt", "rb")
new = open("marks_backup.txt", "wb")
new.write(old.read())
old.close()
new.close()

print(os.path.exists("student_report.txt"))
with open("student_report.txt") as file:
    print(file.read())

print("---- json and pickle ----")
student = {"name": "Jophin", "marks": 85, "subjects": ("Maths", "Science")}

with open("student.json", "w") as file:
    json.dump(student, file)
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print(open("student.json").read())
print(open("student.pkl", "rb").read())

with open("student.json") as file:
    print(json.load(file))
with open("student.pkl", "rb") as file:
    print(pickle.load(file))

print("---- pickle vs json ----")
print("Pickle: binary, Python only, stores any Python object, not human readable")
print("JSON  : text, works with any language, human readable, only simple data types")

print("---- directory contents ----")
print(sorted(os.listdir()))
