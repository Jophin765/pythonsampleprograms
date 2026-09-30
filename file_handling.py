#File handling allows Python programs to store data permanently, read external files,and interact with the operating system.

store_data=open("new_file.txt","w") #file automatically created when given w and then write
store_data.write("Welcome to python programs")
print(store_data)
store_data.close()

append_data=open("new_file.txt","a")
append_data.write("\nPython is an intepreted language")
print(append_data)
append_data.close()

read_data=open("new_file.txt","r")
print(read_data.read())
read_data.close()

#using context manager  # using this file automatically closes
with open("new_file.txt","r") as f:
    print("current position: ",f.tell())
    f.read(6)
    
    print("after read position is: ",f.tell())
    
    f.seek(4)
    print("After seek: ",f.tell())
    print(f.read())

with open("flower.jpeg","rb") as data: #read bytes
    print(data.read())

data=open("delete_file.txt","x")  #exclusive creation 
print(data)
data.close()

file_path="delete_file.txt"
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted succesfully")
else:
    print("File doesnt exist")

#serialization:- 2 ways, pickles and json

import pickle
data={
    "students":["anya","ben","cyan","dona"]
}


#serialization saving data to file
with open("user_details.pkl","wb") as f:  #pickle extension is pkl,wb=write bytes
    pickle.dump(data,f)  #dump should mention what and where to dump
    print("data is serialized to user details")

#deserialization:- retrieving data from file
with open("user_details.pkl","rb") as f:  
    pickle.load(f) 
    print("data is deserialized from user details")

#serialization saving data into memory 
dump_data=pickle.dumps(data)
print("data is serialized into bytes: ",dump_data)

load_data=pickle.loads(dump_data)
print("deserialized data to bytes: ",load_data)

'''