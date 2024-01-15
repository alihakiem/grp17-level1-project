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
