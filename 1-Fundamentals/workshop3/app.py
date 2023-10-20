"""
Workshop 3
By Shosuke Doi
Date 10/15/2023
"""

from donation_pkg.homepage import show_homepage, donate, show_donations
from donation_pkg.user import login, register

database = {"admin": "123"}
donations = []
authorized_user = ""

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    option = input("Choose an option: ")

    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user:
            database = {username: password}
    elif option == "3":
        if authorized_user:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
        else:
            print("You are not logged in")
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        break
    else:
        print("You entered wrong option")
