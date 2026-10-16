#write a program to demonstrate bank operations using list and tuples,deposit,withdraw,balance.in ""tuple inside list method""" 
#tupple store= a/c name,pan card,a/c no.=1000,DOB
#LIST= email-id,contact no.,address,current balance for py program. 

bank = []

n = int(input("Enter number of customers: "))

for i in range(n):
    print("\nEnter details of customer", i + 1)

    name = input("Enter name: ")
    pan = input("Enter PAN card number: ")
    accno = input("Enter account number: ")
    dob = input("Enter date of birth: ")

    email = input("Enter email ID: ")
    contact = input("Enter contact number: ")
    address = input("Enter address: ")
    balance = float(input("Enter current balance: "))

    customer = [
        (name, pan, accno, dob),
        [email, contact, address, balance]
    ]

    bank.append(customer)

print("\n----- BANK DETAILS -----")

for customer in bank:
    print(customer)

print("\n----- BANK MENU -----")
print("1. Deposit")
print("2. Withdraw")
print("3. Display Account Details")

choice = int(input("Enter your choice: "))

if choice == 1:
    accno = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))

    for customer in bank:
        if customer[0][2] == accno:
            if amount > 0:
                customer[1][3] += amount
                print("Deposit successful!")
                print("Current balance:", customer[1][3])
            else:
                print("Invalid amount!")
            break
    else:
        print("Account not found!")

elif choice == 2:
    accno = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))

    for customer in bank:
        if customer[0][2] == accno:
            if 0 < amount <= customer[1][3]:
                customer[1][3] -= amount
                print("Withdrawal successful!")
                print("Current balance:", customer[1][3])
            else:
                print("Invalid amount or insufficient balance!")
            break
    else:
        print("Account not found!")

elif choice == 3:
    print("\n----- BANK DETAILS -----")

    for customer in bank:
        print(customer)

else:
    print("Invalid choice!")