
emp_ids_list = [101,102, 103]
emp_names_list= ['Ahmed','Omar', 'Sarah']

person_dic = {}
person_dic[101] = 'Ahmed'
for i in range(len(emp_ids_list)):
    person_dic[ emp_ids_list[i] ] = emp_names_list[i]
print(person_dic)