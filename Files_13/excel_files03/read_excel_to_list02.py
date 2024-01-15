#program to read from excel and write back to list
import csv
people_list = []

with open("C:\\MY_FILES\\people.csv",'r')as my_file:
    read_from_excel = csv.reader(my_file)
    for line in read_from_excel:
        people_list.append(line)
print(people_list)