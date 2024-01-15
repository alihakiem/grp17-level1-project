password = "alphabet123"
times_left = 3
while times_left > 0 :
    user = input("Please write your password! ")
    if user == password:
        print("You have access")
        break
    else:
        times_left = times_left - 1
        print("incorrect password")
else:
    print("Please try again later your acount is suspended")