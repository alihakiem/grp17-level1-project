with open("C:\\MY_FILES\\write_data.txt",'r') as my_file:
    content = my_file.read()
    print(content)
with open ("C:\\MY_FILES\\write2.txt",'w') as my_file:
    my_file.write(content)


