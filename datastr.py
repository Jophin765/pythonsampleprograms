#string-immutable data
#list-[] ordered collection , mutable,allow dulpicates ,can be accesed using indexing
#tuple-()ordered collection ,immutable,allow dulpicates ,can be accesed using indexing
#set-{}undorederd collection,mutable,doesnt allow duplicates,cannot be accesed using indexing
#dictionary-{key:value}ordered collection,value can be changed,allow duplicate values,can be accesed using key
"""
username="Jophin"

#Indexing
#  0    1  2   3   4    5 positive indexing
# -6  -5  -4  -3  -2  -1  negative indexing starts from right side and -1 as starting point      
#J o p h i n
#Length
#1 2 3 4 5 6

print(username[2])
print(len(username))
print(username[-2])

# String Slicing
# [start:stop:step] step or skip value
# start- start default value is 0
# stop- value -1
# step- no of skip(defaultly 1 for postitve no )

data="Python is A Programming language"
print(data[1:8])
print(data[2:8])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2]) #will not work because due to starting from 10 - 1
print(data[10:1:-2])
print(data[::-2])
print(data[::-1])

#String methods
text="python Nigger"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

print(text.startswith("py"))#Checks Whether given letter starts with given letter
print(text.endswith("er"))
print(id(text))
uppercase=text.upper()
print(id(uppercase))

#List
userdata=["Jophin",21,"Tvm"]
print(userdata)
userdata.insert(1,"MIC")
userdata.append(2026)
userdata.extend("Pi")
userdata.append(["Eng","hindi","Mal"])
print(userdata)
userdata.extend(["html","css"])
print(userdata)
userdata[0]="John"
print(userdata)
userdata.remove("Tvm")
print(userdata)
userdata.pop(6)
print(userdata)
userdata.reverse()
print(userdata)

#tuple - immutable data structure
tuple=(1,2,3,4,5)
print(tuple)

#nested tuple
tuple2=("joe","jose","c.c",(7,8,9))
print(tuple2)

#tuple unpacking
person=("Jophin",21,"TVm")
name,age,place=person
print(name)
print(place)

num=(10,20,30,40,50)
a,b,*c=num
print(c)
print(a)
print(b)

num1=(10,20,30,40,50)
f,*g,h=num1
print(f)
print(g)

num2=(1,25,56,48,68,78)
print(num2.count(56))#counts how many 56 are there
print(num2.index(48))#to know the position of that element
print(num2[2])

name=input("Enter a string: ")
count=0
for char in name:
    count+=1
print("the count is ",count)


user_input=input("enter a string: ")
for letter in user_input:
    if user_input.count(letter)==1:
        print("first non-repeating character is: ",letter)
        break
else:
        print("no non-repeating characters")



#set-{} unordered collection of mutable ones,no duplicates
student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","Python"}
student3={"Python","Urudu"}
student1.add("C")
#student1.add("Kannada","Marathi")
student1.update(["c","java"])
student1.pop()
student1.discard("Arab")
print(student1)


#union

print(student1.union(student2))
print(student1|student2)

#intersection
print(student1.intersection(student2))
print(student1&student2)

#difference
print(student1.difference(student2))
print(student1-student2)

print(student1.symmetric_difference(student2))

#frozenset
fs1=frozenset("Jophin")
fs2=frozenset([1,7,5,1,2,7])
print(fs1)
print(fs2)
"""
#Dictionary
student={
    "name":"jophin",
    "age":21,
    "place":"Tvm",

}

print(student)
print(student["name"])

info=dict(city="tvm",state="kerala")  # noqa: C408
print(info)

print(info.keys())
print(info.values())

student.pop("age")
print(student)

for key,value in student.items():
    if key=="name":
        print(key,value)

#nested dict

employee={
    "emp1":{
        "name": "jophin",
        "age":21,
    },
    "emp2":{
        "name":"eve",
        "age":22,
    },
    "emp3":{
        "name":"c.c",
        "age":1000
    },

}
print(employee["emp1"]["age"])
