#program to write into text file
"""
1.open for write
2.write
3.close
"""
print('-----first way-----')
my_file = open("C:\\MY_FILES\\write_data.txt",'w')
my_file.write('I like programming\n')
my_file.write('I like football\n')
my_file.write('Python is a programming language\n')
my_file.close()
with open("C:\\MY_FILES\\write_data.txt",'a') as my_file:
    my_file.write('My city is cairo\n')
    my_file.write('My city is Alex\n')
    my_file.write('I am a SW Engineer')
