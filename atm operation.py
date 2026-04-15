
correct_pin = "1234"
balance = 1000.0   


for attempt in range(3):
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("Login successful!\n")
        break
    else:
        print("Incorrect PIN")

else:
    print("Account locked due to 3 incorrect attempts.")
    exit()

while True:
    print("\nATM Menu")
    print("1: Check Balance")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("4: Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your current balance is: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))


        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount. Enter a positive value.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount. Enter a positive value.")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
