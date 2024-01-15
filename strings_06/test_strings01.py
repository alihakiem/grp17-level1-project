#show program functions
'''
print("------Create and print strings--------")
emp_name = "Yahia Momtaz"
print(emp_name)
print(type(emp_name))

print("---------upper() , lower() funtions---------")
upper_imp_name = emp_name.upper()
lower_imp_name = emp_name.lower()
print(upper_imp_name)
print(lower_imp_name)
print(emp_name)

print('----------isupper() , islower() ,isalpha functions------true ,false------')
print(emp_name.isupper())
print(emp_name.islower())
print(emp_name.isalpha())
print("---------------endsWith() function-------------")
file_path = 'c:/my_document/egypt.pdf'
file_path = file_path.lower()
if file_path.endswith('pdf'):
    print("It is a book")
elif file_path.endswith('jpg') or file_path.endswith('png'):
    print("It is an image")
else:
    print('Unknown file type')
print("--------------------startswith() function------------------")
emp_mobile = "+96610935325"
if emp_mobile.startswith("+20"):
    print("It is an egyptian mobile")
elif emp_mobile.startswith("+966"):
    print("It is a saudi mobile")
else:
    print("It's an unknown number")

print('-------------in membership----------')
'''
emp_cv = 'i am a programmer , i am interested in java,python,c++'
if 'python' in emp_cv and 'java' in emp_cv:
    print('This emp is the wanted one')
else:
    print("This is not the required emp")
print(emp_cv.count('python'))
print('---------------index(),replace() functions | slicing-------------------')
emp_email = 'yahia.momtaz.hussein@hotmail.com'
user_name = emp_email[0:emp_email.index('@')]
print(user_name)
domain_name = emp_email[emp_email.index('@')+1: ]
print(domain_name )
real_name = user_name.replace('.',' ')
print(real_name)

print('---------Looping : Loop over letters of string--------------')
#for each
for letter in emp_email:
    print(letter)
print('---------------for i with string--------------')
for i in range(len(emp_email)):
    print(emp_email[i])
print('----split the string into list of words--------')
my_courses = 'java python oracle linux network'
courses_list = my_courses.split()
courses_list.reverse()
print(courses_list)
print('--------return the list back to string')
new_courses = ' '.join(courses_list)
print(new_courses)

print('----------strip(),title(),swapcase(),find(),rfind() Self study-------------')
