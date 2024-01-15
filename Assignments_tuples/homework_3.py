Male_count = 0
Female_count = 0
company_employees = [
(101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
(102, 'Ibrahim Ahmed', 9000.0, 'Accountant','M'),
(103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
(104, 'Islam Hasan', 7000.0, 'Sales', 'M'),
(104, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
(104, 'Ola Hasan', 7000.0, 'Engineer', 'F')
]
for employee in company_employees:
    if employee[4] == 'F':
        Female_count = Female_count + 1
    else:
        Male_count = Male_count + 1
print('The number of male employees is :' ,Male_count)
print('The number of male employees is :' ,Male_count)
print('The number of female employees is :' ,Female_count)
