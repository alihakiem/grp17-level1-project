#program to check for person age
#inputs
person_name = 'Ali Ahmed'
person_age = input('Enter your age ')
person_age= int(person_age)
if person_age > 16:
    print('you are a man')
elif person_age >= 11:
    print('You are a boy')
else:
    print('You are a child')
