def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    attempts = 3

    while attempts > 0:
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("Invalid Credentials. Remaining attempts:", attempts)
                username = input("Enter username: ")
                password = input("Enter password: ")

    print("Account Locked")


user = input("Enter username: ")
pwd = input("Enter password: ")

login(user, pwd)