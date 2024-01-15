#program to write a list to excel file
import csv

people_list = [
    ['Name','Age','City'],
    ['Adham',25,'Assiut'],
    ['Essam',30,'Cairo'],
    ['Shady',30,'Mansoura']
]
with open("C:\\MY_FILES\\people.csv",'w',newline='') as my_file:
    write_to_excel = csv.writer(my_file)
    for person in people_list:
        write_to_excel.writerow(person)
