numbers_list = [7, 12, 8, 20, 9, 14]
print(numbers_list)
print(type(numbers_list))
print('2. adding element to list [append fucntion or insert fumction]')
numbers_list.append(11)
numbers_list.insert(1, 77)
print(numbers_list)
print('----3.Access element by index and change it----')
numbers_list[4] = 22
print(numbers_list)
print(numbers_list[4])
print('-----4.count elements of list --> Len function :General function----')
print(len(numbers_list))
print('----------5. delete element from the list --remove, pop functions-----')
numbers_list.remove(9)
print(numbers_list)
numbers_list.pop(4)
print(numbers_list)
print('--------6.reverse list----------')
numbers_list.reverse()
print(numbers_list)
print('------7.sort list--------')
numbers_list.sort(reverse=True)
print(numbers_list)