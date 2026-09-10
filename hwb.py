def create_account(name, account_type="Savings"):
    print("Account Details")
    print("Name :", name)
    print("Account Type:", account_type)
    return name

def customer_details(**data):
    print("Customer Details:")
    for key, value in data.items():
        print(" ", key, ":", value)


def deposit(balance, amount):
    new_balance = balance+amount
    return new_balance


def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance")
        return balance
    else:
        new_balance = balance-amount
        return new_balance


def check_balance(balance):
    return balance


def transaction_history(*transactions):
    print("Transaction Summary")
    print("Transactions:", transactions)
    print("Total Transacted Amount:", sum(transactions))


def loan_eligibility_check(balance, salary, cibil_score=650):
    if balance >= 5000 and salary >= 15000 and cibil_score >= 600:
        return True
    else:
        return False

calculate_interest = lambda amount: amount * 0.05

def verify_pin(correct_pin, attempt=1):
    if attempt > 3:
        print("Maximum Attempts Reached")
        return False
    print("PIN Verification Attempt:", attempt)
    entered_pin = input("Enter PIN: ")
    if entered_pin == correct_pin:
        print("PIN Verified")
        return True
    else:
        return verify_pin(correct_pin, attempt + 1)


account_balances = [15000, 8000, 20000, 25000]
customer_names = ["Joe", "John", "Joseph","Hosea"]
transactions_list = []


def main():
    balance = 10000          
    salary = 25000

    while True:
        print("------ ONLINE BANKING SYSTEM ------")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        
        if choice == "1":
            name =input("Enter Customer Name: ")
            account_type =input("Enter Account Type (Savings/Current): ")
            customer_names.append(name)

            create_account(name, account_type)

            age = input("Enter Age: ")
            city = input("Enter City: ")
            customer_details(name=name, age=age, city=city)

    
        elif choice == "2":
            amount = int(input("Enter Deposit Amount: "))

            balance = deposit(balance=balance, amount=amount)

            transactions_list.append(amount)
            account_balances.append(balance)

            print("Amount Deposited Successfully")
            print("Updated Balance:", balance)
            print("Loan Eligibility:", loan_eligibility_check(balance, salary))
            print("Interest Calculation using Lambda:")
            print(calculate_interest(amount))
            print("Sorted Account List (Balances > 10000):")
            print(sorted(filter(lambda x: x > 10000, account_balances)))
            print("Sorted Customer Names:")
            print(sorted(customer_names))

            verify_pin("1234")

        elif choice == "3":
            amount = int(input("Enter Withdraw Amount: "))

        
            balance = withdraw(balance, amount)

            transactions_list.append(-amount)
            print("Updated Balance:", balance)

        elif choice == "4":
            print("Current Balance:", check_balance(balance))

        
        elif choice == "5":
            transaction_history(*transactions_list)

        elif choice == "6":
            print("Thank you for banking with us")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()