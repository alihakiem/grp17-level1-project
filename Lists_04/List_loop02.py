numbers_list = [7, 12, 8, 20, 9, 14, 9]
sum_list = 0
'''
print('-----1.for i loop-----')
for i in range(len(numbers_list)):
    print(i , '-->' , numbers_list[i])
    sum_list = sum_list+numbers_list[i]
print('sum of elements = ',sum_list)
print("------------2.for each loop[for in loop]:Doesn't use list index-------------")
'''
sum_list = 0
for item in numbers_list:
    print(item)
    sum_list = sum_list + item
print(sum_list)
