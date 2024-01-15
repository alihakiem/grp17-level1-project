persons_list = [{101:'Farouk', 102: "Marwa", 103:"Mostafa"}]
print(persons_list)
print(persons_list[0])
print(persons_list[0][102])
persons_list[0][102] = 'Marwa Mahmoud'
print(persons_list)
print('--------------Adding second dict to the list----------------')
dict2 = {104:"Ibrahim", 105:"Usama Khalil"}
persons_list.append(dict2)
persons_list[1][106] ="Ehab"
print(persons_list[1    ])