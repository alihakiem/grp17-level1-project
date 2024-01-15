def password_verify(pass_value):
    if len(pass_value) < 8:
        return False
    small, capital, special, count_digits = 0, 0, 0, 0
    for letter in pass_value:
        if letter.islower():
            small += 1
        elif letter.isupper():
            capital += 1
        elif letter.isdigit():
            count_digits += 1
        elif letter in '_@$':
            special += 1
    return small>0,capital>0,special>0,count_digits>0

password = "Ali_Ahhmed@2007"
result = password_verify(password)

if result:
    print("Password is valid.")
else:
    print("Password is invalid.")