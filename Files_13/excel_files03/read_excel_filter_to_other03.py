#program to read from excel and filter data and write to another
import csv
with open("C:\\MY_FILES\\people.csv",'r')as my_file,\
     open("C:\\MY_FILES\\people_filtered.csv",'w',newline='') as my_file2:
    read_from_excel = csv.reader(my_file)
    write_to_excel = csv.writer(my_file2)
    write_to_excel.writerow(['Name',"Age","City"])
    for row in read_from_excel:
        if row[2] == "Cairo":
            write_to_excel.writerow(row)
