from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with a starting balance of {balance}")

while True:
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.showBalance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.showBalance(balance)
    elif option == "3":
        _ = account.withdraw(balance)
        if isinstance(_, str):
            print(_)
        else:
            balance = _
            account.showBalance(balance)
    else:
        account.logout(name)
        break
