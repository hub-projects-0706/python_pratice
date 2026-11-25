amount = 50000
pin_number = 1425
attempt=3
transactions = []
def pin_attempt():
    for i in range(3):
        pin = int(input("Enter your PIN: "))
        if pin == pin_number:
            return True
        else:
            print("Invalid PIN!")
            print("Attempts remaining:", 2-i)
    return False


def width_draw(amount):
    a = int(input("Enter amount: "))

    if a <= 0:
        print("Enter a valid amount!")

    elif a <= amount:
        amount = amount - a
        transactions.append(
            f"Withdrawn: {a} | Balance: {amount}"
        )
        print("Withdrawal Successful!")

    else:
        print("Insufficient Balance!")

    return amount


def deposit_money(amount):
    am = int(input("Enter the Amount to deposit: "))

    if am <= 0:
        print("Enter a valid amount!")

    else:
        amount = amount + am
        transactions.append(
            f"Deposited: {am} | Balance: {amount}"
        )
        print("Deposit Successful!")

    return amount


def mini_statement(amount):
    print("\n------ MINI STATEMENT ------")
    print("Acc_no: xxxxxxxxxx800")
    print("Name: Ruthra")
    print("Balance:", amount)

    print("\nRecent Transactions:")

    if len(transactions) == 0:
        print("No transactions found!")

    else:
        for t in transactions[-5:]:
            print(t)

    print("----------------------------")

print("Welcome to ATM Bank!")
print("Insert your ATM Card")

while True:
    print("\nSelect your language:")
    print("1. English")
    print("2. Exit")

    lan_choice = int(input("Enter choice: "))

    if lan_choice == 1:

        print("\nSelect Your Banking Operations:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit money")
        print("4. Mini Statement")
        print("0. Exit")

        ope_choice = int(input("Enter choice: "))

        if ope_choice == 1:
            if pin_attempt():
                print("--------------------------")
                print("Acc_no: xxxxxxxxxxx800")
                print("Location: Dindigul")
                print("Balance:", amount)
                print("--------------------------")
        elif ope_choice == 2:
            if pin_attempt():
                amount = width_draw(amount)
            else:
                print("bye!!!")
                break
        elif ope_choice==3:
            if pin_attempt():
                amount=deposit_money(amount)
            else:
                print("bye!!!")
                break           
        elif ope_choice==4:
            if pin_attempt():
                mini_statement(amount)
            else:
                print("bye!!!")
                break
        elif ope_choice ==0:
            print("Thank You!")
            break
        else:
            print("Invalid operation!")

    elif lan_choice == 2:
        print("Thank you for using ATM Bank!")
        break
    else:
        print("Invalid language choice!")
