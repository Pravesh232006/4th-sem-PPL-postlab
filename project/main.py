from bank import BankAccount
from validator import validate_email, validate_userid

print("=== Registration ===")

name = input("Enter name: ")
email = input("Enter email: ")
uid = input("Enter user id: ")

if not validate_email(email):
    print("Invalid email")
    exit()

if not validate_userid(uid):
    print("Invalid user id")
    exit()

balance = float(input("Enter initial balance: "))
pin = input("Set PIN: ")

acc = BankAccount(name, balance, pin)

while True:
    print("\n--- BANK MENU ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    entered_pin = input("Enter PIN: ")

    if not acc.check_pin(entered_pin):
        print("Wrong PIN")
        continue

    if ch == 1:
        acc.show_balance()

    elif ch == 2:
        amt = float(input("Enter amount: "))
        acc.deposit(amt)

    elif ch == 3:
        amt = float(input("Enter amount: "))
        acc.withdraw(amt)

    elif ch == 4:
        amt = float(input("Enter amount: "))
        acc.transfer(amt)

    else:
        print("Invalid choice")