try:
    firstname = input("first name: ")
    secondname = input("second name: ")
    age = int(input("your age: "))
    welcome_message = "Welcome {} {} you are {} years old".format(firstname,secondname,age)
    print((welcome_message))
except ValueError:
    print("please enter your age in numbers the next time")

