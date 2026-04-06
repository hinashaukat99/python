correct_password = "1234"
count = 3
while count > 0:    
    password = input("enter ur password")
    if password == correct_password:
        print("Access granted")
        break
    else:
        count -= 1
        print("Wrong Password, Remainig Attempts" , count)
if count == 0:
    print("Account Locked")

        