try:
    a = int(input("Enter an integer: "))
except ValueError:
    while ValueError :
        a = input("Enter an integer: ")
        if a.isdigit() == False:
            continue
        else:
            break