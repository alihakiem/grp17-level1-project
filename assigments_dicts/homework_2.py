person_1_tuples = (101,'Ahmed Essam',5000.0,'Cairo','0124395892234')
person_2_tuples = (102, 'Mohamed Omar',6000.0,'Alex','011249529359')
person_3_tuples = (103,'Ibrahim Hesham',7000.0,'Portsaid','01024583204')
combined_dictionary = {}
for person_id,name,salary,city,phone in [person_1_tuples,person_2_tuples,person_3_tuples]:
    combined_dictionary[person_id] = {'name' :name,'salary' : salary,'city' : city,'phone': phone}
print(combined_dictionary)