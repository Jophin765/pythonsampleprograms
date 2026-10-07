"""
numberlist = []
number_of_elements = int(input("Enter the number of elements in the list: "))
for element in range(number_of_elements):
    num = int(input(f"Enter the element: {element+1}: "))
    numberlist.append(num)

largest_num = numberlist[0]
smallest_num = numberlist[0]
for num in numberlist:
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num
print("The largest number in the list: ", largest_num)
print("The smallest number in the list: ", smallest_num)

# 13 5 6 7 8
#largest =13
#smallest=13
#num=13
#1.first iteration num>largest-false,num<smallest-false
#2.second iteration num=5,largest=13,smallest=13 True smallest = 5
#3.third iteration num=6,largest=13,smallest=5 False
#4.fourth iteration num=7,largest=13,smallest=5 False
#5.fifth iteration num=8,largest=13,smallest=5




# number of occurence of given no in a tuple

count = 0
numbers = tuple(map(int, input("Enter the numbers to be inserted: ").split()))
number_to_check = int(input("Enter the number to count: "))
for element in numbers:
    if element == number_to_check:
        count += 1
print(f"Occurence of {number_to_check} in tuple is {count}")


# reverse the dictionary
data = {"a": 1, "b": 2, "c": 3}
reversed_data = {}
reversed_keys = list(data.keys())  # a["a","b","c"]
for key in reversed_keys[::-1]:
    reversed_data[key] = data[key]
print(reversed_data)


# separate list of elements as positive and negative numbered list
numbers = [12, -5, 8, -1, 0, 45, -30, 7]

positive_list = []
negative_list = []

for element in numbers:
    if element > 0:
        positive_list.append(element)
    else:
        negative_list.append(element)

print("Positive:", positive_list)
print("Negative:", negative_list)



# linear search
user_marks = list(map(int, input("Enter no of numbers to be inserted:").split()))
search_element = int(input("Enter the element to be search:"))
for i in range(len(user_marks)):
    if search_element == user_marks[i]:
        print(f"Element found at index {i}")
        break
else:
        print("Element not found")

# fibonacci series
# 0 1 1 2 3 5 8 13
# 0=1,b=1,c=0+1=1
# a=b,b=c,c=1+1=2
# a=1,b=2,c=2+1=3

a = 0
b = 1
number_of_iterations = int(input("
Enter the number of iterations:"))
for element in range(number_of_iterations):
    print(a)
    c = a + b
    a = b
    b = c

#prime numbers
number = int(input("Enter the number:"))
for i in range(2, number):
    if number % i ==0:
        print("Not prime")
        break
else:
    print("Prime")
 



#Bubble Sort
def bubblesort(num):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                temp=num[i]
                num[i]=num[j]
                num[j]=temp
    return num
print(bubblesort([3,2,1,5,6,4]))


#Pattern 
number=int(input("Enter the number:"))
for row in range(1,number+1):
    for column in range(1,number+1):
        print("*",end="")
    print()

#Numbers Col
number=int(input("Enter the number:"))
for row in range(1,number+1):
    for column in range(1,number+1):
        print(column,end="")
    print()

#Left Side
number=int(input("Enter the number:"))
for row in range(1,number+1):
    for column in range(1,row+1):
        print("*",end="")
    print()


number=int(input("Enter the number:"))
for row in range(1,number+1):
    for column in range(1,number+1):
        if row<=column:
            print(row,end="")
        
    print()


numbers=[1,7,8,2,4]
result=tuple(x**2 for x in numbers)
print(result)


cubes={item:item**3 for item in range(1,11)}
print(cubes)



elements=[2,4,2,6,7,9]
even_numbers={item for item in elements if item%2==0}
print(even_numbers)


list_of_names=["John","C.C","Rize"]
uppercase=[item.upper() for item in list_of_names]
print(uppercase)
check_letter=[item for item in list_of_names if "C" in item]
print(check_letter)


texts="Python programming"
vowels=[item for item in texts if item in "aeiou"]
print(vowels)
unique={item for item in texts}
print(unique)

asci_code={item:ord(item) for item in texts} #ord => to generate asci code
print(asci_code)



languages=["Python","Java","C++"]
lengths=[len(item) for item in languages]
print(lengths)
first_letter=[item[0] for item in languages]
print(first_letter)
first_char_with_length=[(item,len(item)) for item in languages]
print(first_char_with_length)
"""
