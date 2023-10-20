def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("Welcome back admin!")
            return username
        else:
            print("Incorrect password for admin")
            return ""
    else:
        print("User not found. Please register")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"Username {username} registered")
        return username
