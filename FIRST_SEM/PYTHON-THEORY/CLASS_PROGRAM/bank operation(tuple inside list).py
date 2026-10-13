# Bank Operations using Tuple inside List

name = input("Enter Account Name: ")
pan = input("Enter PAN Card Number: ")
account_no = int(input("Enter Account Number: "))
dob = input("Enter Date of Birth: ")

email = input("Enter Email ID: ")
contact = input("Enter Contact Number: ")
address = input("Enter Address: ")
balance = float(input("Enter Current Balance: "))

account_info = (name, pan, account_no, dob)
bank_data = [email, contact, address, balance]
bank_account = [account_info, bank_data]

while True:
    print("\n===== BANK OPERATIONS =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            bank_account[1][3] += amount
            print("Deposit successful!")
            print("Current Balance:", bank_account[1][3])
        else:
            print("Invalid deposit amount.")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > bank_account[1][3]:
            print("Insufficient balance.")
        else:
            bank_account[1][3] -= amount
            print("Withdrawal successful!")
            print("Current Balance:", bank_account[1][3])

    elif choice == 3:
        print("Current Balance:", bank_account[1][3])

    elif choice == 4:
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Name  :", bank_account[0][0])
        print("PAN Card      :", bank_account[0][1])
        print("Account No.   :", bank_account[0][2])
        print("Date of Birth :", bank_account[0][3])
        print("Email ID      :", bank_account[1][0])
        print("Contact No.   :", bank_account[1][1])
        print("Address       :", bank_account[1][2])
        print("Balance       :", bank_account[1][3])

    elif choice == 5:
        print("Thank you for using the bank application.")
        break

    else:
        print("Invalid choice.")