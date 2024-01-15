#to show how to handle exceptions
import sys

try:
    first_number = int(input('Please enter first number: '))
    second_number = int(input('Please enter second number: '))
    result = first_number / second_number
    print('result = ', result)
    open('C:\\my_files\\edu.txt')
except ValueError:
    print("Please only enter numbers")
except ZeroDivisionError:
    print('Cannot divide by Zero')
except Exception as error_msg:
    print("There is something wrong,contact admin or try again later.")
    print(error_msg)
finally:
    print("This is the finally statement-works any time")
print('Continue or End the program 5')