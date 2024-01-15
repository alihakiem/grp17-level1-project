company_employees = [
    (101, 'Ahmed Esam', 10000.0, 'Cairo'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
    (103, 'Adham Aly', 5000.0, 'Cairo'),
    (104, 'Islam Hasan', 7000.0, 'Cairo')
]

sum = 0

for employee in company_employees:
    sum += employee[2]

print("Total salary of all employees:", int(sum))
