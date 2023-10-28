"""
Week 4 workshop
By: Shosuke Doi
Version 1.3
Last Updated: 10/21/2023
"""


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name}'s balance: {float(self.balance)}")

    def withdraw(self, value):
        print(value)
        self.balance = self.balance - value

    def deposit(self, value):
        self.balance = self.balance + value

    def transfer_money(self, recepient, value):
        pin = input("Enter your PIN: ")
        if int(pin) == self.pin:
            self.withdraw(value)
            recepient.deposit(value)
            return True
        else:
            print("Invalid PIN. Transaction canceled")
            return False

    def request_money(self, sender, value):
        pin = input("Enter your PIN: ")
        if int(pin) == self.pin:
            password = input("Enter your password: ")
            if password == self.password:
                self.deposit(value)
                sender.withdraw(value)
                return True
            else:
                print("Invalid password. Transaction canceled")
                return False
        else:
            print("Invalid PIN. Transaction canceled")
            return False


""" Driver Code for Task 1 """

# user = User("Sho", 1234, "password")
# print(f"name: {user.name} / pin: {user.pin} / password: {user.password}")

""" Driver Code for Task 2 """

# user = User("Sho", 1234, "password")
# print(f"name: {user.name} / pin: {user.pin} / password: {user.password}")
# user.change_name("Doi")
# user.change_pin(12)
# user.change_password("pass")
# print(f"name: {user.name} / pin: {user.pin} / password: {user.password}")

""" Driver Code for Task 3"""

# bank_user = BankUser("Sho", 1234, "password")
# print(
#     f"name: {bank_user.name} / pin: {bank_user.pin} / password: {bank_user.password} / balance: {bank_user.balance}"
# )

""" Driver Code for Task 4"""

# bank_user = BankUser("Sho", 1234, "password")
# bank_user.show_balance()
# bank_user.deposit(100)
# bank_user.show_balance()
# bank_user.withdraw(50)
# bank_user.show_balance()

""" Driver Code for Task 5"""

bank_user = BankUser("Sho", 1234, "password")
bank_user2 = BankUser("Sho2", 12, "pass")

bank_user2.deposit(5000)
# bank_user2.show_balance()
# bank_user.show_balance()

is_transfer_successful = bank_user2.transfer_money(bank_user, 500)
bank_user.show_balance()
bank_user2.show_balance()

if is_transfer_successful:
    bank_user2.request_money(bank_user, 250)
    bank_user2.show_balance()
    bank_user.show_balance()
