numbers_list = [1,2,3,4,5,6]
even_numbers = []
for number in numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)
if even_numbers:
    print(even_numbers,"are even numbers")
else:
    print("There are no even numbers")


