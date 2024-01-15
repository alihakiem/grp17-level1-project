def find_double(my_list,num):
    test_list =[]
    for test_num in range(len(my_list)):
        if my_list[test_num]==num:
            test_list.append(test_num)
    return test_list
my_list =[1,3, 4, 2, 5, 2, 6]
num = 2
answer=find_double(my_list,num)
print(answer)
