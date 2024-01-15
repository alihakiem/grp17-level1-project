try:
    def divide_numbers(a, b):
        answer = a/b
        print(answer)
    divide_numbers(10,2)
except ZeroDivisionError:
    print("Division by zero is not allowed!")

