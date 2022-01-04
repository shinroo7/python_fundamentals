# learn how to r (read), w (write), a (add appendex), r+ (read & write)

#read
employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()


#write: over write a file or create a new file 
#append: to add data in the file

employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service") #use \n to add a new line

employee_file.close()


