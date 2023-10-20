def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations       |")
    print("------------------------------------------")
    print("|            5.    Exit                |")
    print("------------------------------------------")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = f"{username} donated ${float(donation_amt)}"
    print("Thank you for your donation")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations:
        for d_str in donations:
            print(f" - {d_str}")
    else:
        print("Currently, there are no donations.")
