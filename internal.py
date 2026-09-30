# store the name of  patients in a list
patients = ["Copper Vinod", "c.c", "Rize", "LeGoat"]
print("1. patients names:")
for name in patients:
    print(" ", name)
# store patients details in a tuple
patients_details = ("John", 25, "Male", "Heart patient")
print("\n2.Disease of patient : ", patients_details[3])
# store unique diseases names in a set
diseases = {"Heart disease", "Diabetes", "Cancer"}
print("\n3. diseases:")
for disease in diseases:
    print(" ", disease)
# create a frozenset containing hospital rules such as "No smoking","Wear masks"and "maintain silence"
hospital_rules = frozenset(["No smoking", "Wear masks", "maintain silence"])
print("\n4. hospital rules:")
for rule in hospital_rules:
    print(" ", rule)

# write a function calculate_bill(amount)that adds 100 as a service charge and returns final bill
def calculate_bill(amount):
    return amount + 100

print("\n5. calculate bill:")
bill = calculate_bill(100)
print(" ", bill)

# take a patients name and convert it into title case
def title_case(name):
    return name.title()

print("\n6. title case:")
title = title_case("John")
print(" ", title)

# take a patients age.if the age is greater than 60,display"senior citizen"
def senior_citizen(age):
    if age > 60:
        return "senior citizen"
    else:
        return "adult"

print("\n7.senior citizen:")
senior = senior_citizen(65)
print(" ", senior)
