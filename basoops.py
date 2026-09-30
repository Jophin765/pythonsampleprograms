"""
class Car:
    color = "black"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car_object = Car("BmW", "M5")
print(car_object.brand, car_object.model, car_object.color)

car_object1 = Car("Audi", "A4")
print(car_object1.brand, car_object1.model, car_object1.color)


class Library:
    def __init__(self, book, author):
        self.book = book
        self.author = author
        self.count = 0

    def book_count(self, number):
        self.count = number

lib_object = Library("Python", "Tinu")
print(lib_object.book, lib_object.author)

lib_object.book_count(10)
print(lib_object.count)


#1.Inheritance
#Single inheritance
class User:    #Base class or super class
    def login(self):
        print("User Logged in")
class Influencer(User): #Sub class,derived class
    def postreels(self):
     print("Influencer posted a new reel")
inf_obj = Influencer()
inf_obj.login()
inf_obj.postreels()


#multi level inheritance

class Vehicle:
    def category(self, mode):
        print("Mode of transport is", mode)

class Car(Vehicle):
    def vehicle_category(self, category, color):  # Fixed spelling from vehcile_category
        print("Category of vehicle is", category)
        print("Color of vehicle is", color)

class ElectricCar(Car):
    def car_type(self, brand, category, variant, price):
        print(f"Vehicle brand is {brand} and category is {category} and variant is {variant} and price is {price}") # Fixed typo "vebhicle"

ecar = ElectricCar()
ecar.category("Road")
ecar.vehicle_category("Car", "Red")
ecar.car_type("Tesla", "Electric", "Model S", "1000000")


# muliple inheritance
class ImageUpload:
    def uploadimage(self,username,imagename):
        print(f"{username} posted {imagename} successfully")
class ReelUpload:
    def uploadreels(self,reel_title,reel_duration):
        print(f"uploaded reel is {reel_title} of {reel_duration} seconds")
class Instagram(ImageUpload,ReelUpload):
    def user_analytics(self,user_name,owner,reaction):
        print(f"{user_name} is having a {owner} account with {reaction} reactions on post")
insta=Instagram()
insta.uploadimage("jophin","flowers")
insta.uploadreels("python reel","10 seconds")
insta.user_analytics("jophin","meta","10 reactions")





class Account:
    def details(self):
        print("Account details")
class Loan:
    def details(self):
        print("Loan details")
        super().details()
class Customer(Loan,Account):
    def details(self):
        print("Customer details")
        super().details()
customer=Customer()
customer.details()

#hiearchial and hybrid inheritance

#polymorphism - representing single object in many ways
#method overloading- same class,same method,different arguements eg fb log in
#method overriding-different class,same method,different parameters eg acc log in in different apps

class Calculator:
    def sum(self,num1=0,num2=0,num3=0):
        return num1+num2+num3
calucator=Calculator()
print(calucator.sum(1,2,3))

class Facebook:
    def login(self,email=None,password=None,phonenum=None):
        if email and password:
            print(f"login through email id : {email}")
        elif phonenum and password:
            print (f"login through phone number : {phonenum}")
        else:
            print("Invalid login")
facebook=Facebook()
facebook.login(email="jophinkjohny@gmail.com",password="123")
facebook.login(phonenum="1234567890",password="123")


#overriding
class Employee:
    def work(self):
        print("Working as a Employee")

class Manager(Employee):
    def work(self):
        print("Managing team")
        super().work()
manager=Manager()
manager.work()

#Hiearchial Inheritance - one parent inherit multiple childs
class Account:
    def details(self):
        print("Account Details")
class SavingsAccount(Account):
    def details(Self):
        print("savings account details")
        super().details()
class CurrentAccount(Account):
    def details(self):
        print("current account details")
        super().details()
savings=SavingsAccount()
savings.details()
current=CurrentAccount()
current.details()

#Hybrid- its a mix of inheritance eg hiearchial + multiple inheritance
class Loan:
    def details(self):
        print("Loan details")
class PersonalLoan(Loan):
    def details(self):
        print("Personal Loan details")
        super().details()

class Account:
    def details(self):
        print("Account details")
        super().details()
class User(Account,PersonalLoan):
    def details(self):
        print("User details")
        super().details()
user=User()
user.details()



class Anime:
    def details(self, studio, title, genre=None, rating=None):
        if genre and rating:
            print(
                f"The studio is {studio} and title of anime is {title} and genre is {genre} and rating for this anime is {rating}"
            )
            print(f"Remainder that Rating of this anime is {rating}")
        elif studio and title:
            print(f"The {studio} is proudly presenting {title}")
        else:
            print("Invalid details")


anime = Anime()
anime.details("Studio Pierrot", "Bleach TYBW", "Action", 9.7)
anime.details("Studio Pierrot", "Bleach TYBW")



class Persona3:
    def characters(self):
        print("Characters of Persona 3")
class Persona4(Persona3):
    def characters(self):
        print("Characters of Persona 4")
        super().characters()
persona4=Persona4()
persona4.characters()



class Gpay:
    def transaction(self,sender=None,receiver=None,pin=None,amount=None):
        if sender and receiver:
            print(f"The transaction is between {sender} and {receiver}")
        elif pin and amount:
            print(f"the transction of {amount} is sucessfully done and {pin} is verified")
        else:
            print("Invalid transaction")
gpay=Gpay()
gpay.transaction("acer","asus")
gpay.transaction(amount=1000,pin=1234)


class Ytmusic:
    def play(self,artist=None,song=None,genre=None):
        if song and artist:
            print(f"Playing {song} by {artist}")
        elif artist and genre:
            print(f"The User is listening to {genre} music made by {artist}")
        else:
            print("User is sleeping")
ytmusic=Ytmusic()
ytmusic.play("Bury the LIght","Dmc 5")
ytmusic.play(artist="Dmc 5",genre="Edm")

class Driver:
    def work(self):
        print("The driver is working")
class Conductor(Driver):
    def work(self):
        print("The conductor is working")
        super().work()
conductor=Conductor()
conductor.work()

class Hospital:
    def work(self):
        print("The hospital is woking data today")
class Staffs(Hospital):
    def work(self):
        print("All the staffs must be present")
        super().work()
staffs=Staffs()
staffs.work()

class Paytm:
    def transaction(self,sender=None,receiver=None,pin=None,amount=None,phoneno=None):
        if sender and receiver:
            print(f" the {sender} has made transaction with {receiver}")
        elif pin and amount:
            print(f" The amount of {amount} has been transacted and {pin} is verified")
        elif phoneno and receiver:
            print(f"a transaction from {phoneno} has been reached to {receiver}")
        else:
            print("Invalid transaction")
paytm=Paytm()
paytm.transaction("Jophin","John")
paytm.transaction(amount=1000,pin=1234)
paytm.transaction(phoneno="8590347959",receiver="John")


#abstraction- hiding the implementation details
from abc import ABC, abstractmethod

# Caanot instantiate a abstract class

class Vehicle(ABC):

    @abstractmethod
    def start_engine(Self):
        pass

    @abstractmethod #decorator
    def stop_engine(Self):
        pass
class Car(Vehicle):
    def start_engine(Self):
        print("Car started using key ")
    def stop_engine(Self):
        print("Car stopped using key ")
car=Car()
car.start_engine()
car.stop_engine()

#Encapsulation - data hiding mechanism

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #private variable two underscore btw
    def show_age(self):
        print(self.__age)
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be positive")

person=Person("Jophin",21)
print(person.name)
#print(person.age) cannot access due to private variable
person.show_age()
person.set_age(26)
print(person.get_age())


#getter and setter - for updation provided by python itself


from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def start_print_receipt(self):

        pass

    @abstractmethod
    def stop_print_receipt(self):
        pass


class Branch(Bank):
    def start_print_receipt(self):
        print("Branch is printing receipt")

    def stop_print_receipt(self):
        print("Branch is stopping receipt printing")


branch = Branch()
branch.start_print_receipt()
branch.stop_print_receipt()



from abc import ABC, abstractmethod


class Meta(ABC):
    @abstractmethod
    def start_reels(self):
        pass

    @abstractmethod
    def stop_reels(self):
        pass


class Insta(Meta):
    def start_reels(self):
        print("Started watching insta reels")

    def stop_reels(self):
        print("Stopped watching insta reels")
insta=Insta()
insta.start_reels()
insta.stop_reels()
"""