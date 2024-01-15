def sum_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return sum(positive_numbers)

numbers_list = [1, -2, 3, -4, 5]
result_sum = sum_positive_numbers(numbers_list)
print(result_sum)
print("----------------------------------")
def count_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return len(positive_numbers)
numbers_list = [1, -2, 3, -4, 5]
result_count = count_positive_numbers(numbers_list)
print(result_count)