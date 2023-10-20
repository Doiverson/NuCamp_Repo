def showBalance(balance):
    print(f"Current balance: ${float(balance)}")


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + int(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    total = balance - int(amount)
    if total >= 0:
        return total
    else:
        return "Balance is not sufficient"


def logout(name):
    print(f"Goodbye {name}")
