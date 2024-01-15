#question 1
def password_verify(pass_value):
    if len(pass_value) < 8:
        return False
    small, capital, special, count_digits = 0, 0, 0, 0
    for letter in pass_value:
        if letter.islower():
            small += 1
        elif letter.isupper():
            capital += 1
        elif letter.isdigit():
            count_digits += 1
        elif letter in '_@$':
            special += 1
    return small>0,capital>0,special>0,count_digits>0

password = "Ali_Ahhmed@2007"
result = password_verify(password)

if result:
    print("Password is valid.")
else:
    print("Password is invalid.")
#question 2
def reverse_string(statement):
    words_reversing= statement.split()
    reversed_statement = ' '.join(reversed(words_reversing))
    return reversed_statement
str = "i like this program very much"
answer = reverse_string(str)
print(answer)
#question 3
def find_double(my_list,num):
    test_list =[]
    for test_num in range(len(my_list)):
        if my_list[test_num]==num:
            test_list.append(test_num)
    return test_list
my_list =[1,3, 4, 2, 5, 2, 6]
num = 2
answer=find_double(my_list,num)
print(answer)
#question 4
def remove_special(statement):
    clean_str = ""
    for character in statement:
        if character.isalnum():
            clean_str = clean_str + character
    return clean_str
ini_string = "123abcjw:, .@! eiw"
ans = remove_special(ini_string)
print(ans)
#question 5
def remove_extra(ips_list):
    corrct_list = []
    for item in ips_list:
        if item not in corrct_list:
            corrct_list.append(item)
    return corrct_list
ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
result = remove_extra(ips_list)
print(result)
#question 6
male_counts = 0
female_counts = 0
company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
    (104, 'Islam Hassan', 7000.0, 'Sales', 'M'),
    (105, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
    (106, 'Ola Hassan', 7000.0, 'Engineer', 'F')]

for item in company_employees:
    Gender = item[4]
    if Gender == 'F':
        female_counts = female_counts+1
    elif Gender == "M":
        male_counts = male_counts+1
print('male count')
print(male_counts)
print('female count')
print(female_counts)
#question 7
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
sum = 0

for item, price in shopping_cart_dict.items():
    shopping_cart_dict[item] = price + price * 10/100
    sum = sum + shopping_cart_dict[item]

print('raise = ', shopping_cart_dict)
print('sum = ', sum)

net_value = sum + sum * 14/100
print( net_value)
#question 8
def swap_numbers(a, b):
    a, b = b, a
    print('no1 = ',a,'no2 = ',b)

no1 = 5
no2 = 10
swap_numbers(no1,no2)
#question 9
ips_list = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.81', 'n'),
('192.168.0.11', 'y')
]
for ip, num in ips_list:
    if num == 'y':
        print(ip,'->',ip[10:])
#question 10
ips_list = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.81', 'n'),
('192.168.0.11', 'y')
]
for ip, num in ips_list:
    if num == 'y':
        print(ip,'->',ip[10:])