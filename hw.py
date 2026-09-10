customer_name=input("Enter The Customer Name: ") #using for inputing customer name
food_item=input("Enter the Food Item Name: ")   #using for food input
quantity=int(input("Enter the Quantity: "))      #used explicit conversion to read input values in integer values
price_per_item=float(input("Enter the Price per item: "))   #used explicit coversion to read input values in floating point values
distance_km=float(input("Enter the delivery distance in KM: "))
totalfood_cost=quantity*price_per_item
rate_per_km=23.0
delivery_charge=distance_km*rate_per_km
final_bill_amount=totalfood_cost+delivery_charge

print("-------ORDER DETAILS------")

print("Customer Name: ",customer_name)   #used for printing outputs
print("type: ",type(customer_name))
print("id: ",id(customer_name))

print("food item Name: ",food_item)
print("Type: ",type(food_item))
print("id : ",id(food_item))

print("Quantity : ",quantity)
print("type: ",type(quantity))

print("Price Per item : ",price_per_item)
print("type: ",type(price_per_item))


print("delivery charge is: ",delivery_charge)

print("final bill amount is: ",final_bill_amount)
print("type: ",type(final_bill_amount))

print("checking Data types")
print("Quantity is integer: ",isinstance(quantity,int))
print("price is float: ",isinstance(price_per_item,float))
print("Final bill is float: ",isinstance(final_bill_amount,float))