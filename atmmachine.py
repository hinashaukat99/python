
balance = 1000 
def check_balance():
    print("Your current balance is: ", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposited successfully! New balance: ", balance)
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful! Remaining balance: ", balance)
    else:
        print("Insufficient balance!")

def change_pin():
    global pin
    old_pin = input("Enter your current PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")

        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully!")
        else:
            print("PINs do not match!")
    else:
        print("Incorrect current PIN!")

def insert_card():
    card_attempts = 3

    while card_attempts > 0:
        card_number = input("Insert your card (Enter card number): ")

        if card_number == "1234":
            pin_attempts = 3

            while pin_attempts > 0:
                global pin
                pin = input("Enter your PIN: ")

                if pin == "223344":
                    print("Authentication successful!")
                    return True
                else:
                    pin_attempts -= 1
                    print("Incorrect PIN! Attempts left: ", pin_attempts)

            print("Account locked due to too many incorrect PIN attempts!")
            return False

        else:
            card_attempts -= 1
            print("Invalid card! Attempts left: ",card_attempts)

    print("Card blocked due to too many invalid attempts!")
    return False

def atm():
    if not insert_card():
        return  # Stop if authentication fails
    
    while True:
        print("--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change Pin")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            change_pin()
        elif choice == '5':
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice, try again!")

atm()