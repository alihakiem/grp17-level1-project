#find if a no. is found in list -print its first index
#or print no is not found using flag
my_list = [12,5,22,10,30]
num = 22
is_found = False
for item in my_list:
    if item == num:
        print(my_list.index(item))
        is_found = True

if is_found == False:
    print('No. is not found')