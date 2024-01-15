#show all printing
import math

emp_id = 101
emp_name = 'Esam Omar'
emp_salary = 7853.6782123
print('-----------1.print with concat--------')
print('Emp has id : '+str(emp_id)+', his name is '+emp_name+', \n''takes salary : '+str(emp_salary))
print('-------2.print with multi parameters----------------')
print('Emp has id = ', emp_id, 'his name is',emp_name,'takes salary',emp_salary)
print(150,120,200,30,sep='-')
for i in range(11):
    print(i,end=" ")
print('\ntest')
print('test2')
#-------------------------------------------------------------------------------------------------------------------------
print('---------------3.string formatting using placeholders -------%s ,%d,%f')
print("Emp has id = %d ,his name is %s ,takes salary = %f"%(emp_id,emp_name,emp_salary))
#4
print('Emp has id = {:d} ,his name is {:s} ,takes salary = {:,.2f} '.format(emp_id,emp_name,emp_salary))
print('----------5.string formatting using F-string function---------')
print(f'Emp has id {emp_id},his name is {emp_name},takes salary = {emp_salary:,.2f}')

#------------------numbers functions :round,trunc,ceil,floor
emp_salary = 64058205.273280235
print(f'Using round function,result = {round(emp_salary,2)}')
print(math.trunc(emp_salary))
print(math.ceil(emp_salary))
print(math.floor(emp_salary))

