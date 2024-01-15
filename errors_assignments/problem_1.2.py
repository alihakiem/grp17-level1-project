string = ("hello this is the ")
for letter in string:
    if letter.isalnum() != True:
        print(letter)

else:
    print("There are no special characters")