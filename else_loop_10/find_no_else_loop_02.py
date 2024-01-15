#find if a no. is found in list -print its first index
#or print no is not found using an else loop
my_list = [12,5,22,10,30]
num = 24

for item in my_list:
    if num == item:
        print(f"number is found at index {my_list.index(num)}")
        break
else:
    print("no is not found")