#r - read
#r+ - read and write
#w - write
#a - append
employee_file = open('employee.text', 'r')
print(employee_file.readable())
employee_file.close()
