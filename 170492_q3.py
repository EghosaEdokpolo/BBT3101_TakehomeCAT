class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
        #employee details
    def display(self):
        print(f"your name is {self.name}")
        print(f"your employee_id is {self.employee_id}")
        print(f"your salary is {self.salary}")

        #updating salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"\nyour new salary is {self.salary}")
    


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employee_list = []
    
    #method to add new employee
    def add_employee(self, name, employee_id, salary):
        employee = Employee(name, employee_id, salary)
        self.employee_list.append(employee)  
        print(f"\nEmployee {name} added to {self.department_name} department. ID is {employee_id}, his/her salary: {salary}")
    
    #method to calculate salary
    def calculate_salary(self):
        total_sum = sum(employee.salary for employee in self.employee_list)
        print(f"\nTotal salary for the {self.department_name} department is {total_sum}.")
        return total_sum
    
    #method to list passengers
    def list_employee(self):
        for employee in self.employee_list:
            print(f"Name: {employee.name}, Employee ID: {employee.employee_id}, Salary: {employee.salary}")

        #interative code
    def interactive_add(self):
        inp_name = input("what is your name? :")
        inp_id = input("what is your id? :")
        inp_salary = input("what is your salary? :")

        employee = Employee(inp_name, inp_id, inp_salary)

        self.employee_list.append(employee)  
        print(f"\nEmployee {inp_name} added to {self.department_name} department. ID is {inp_id}, his/her salary: {inp_salary}")
    
    #displaying the details for employee
employee = Employee("Alice Johnson", 101, 50000)
employee.display()
employee.update_salary(1000)
    #adding employee to department
dep = Department("HR")
dep.add_employee("mona", 187, 4000)
dep.add_employee("lumine", 110, 4100)
    #calculated salary 
dep.calculate_salary()
    #calling the interactive input
dep.interactive_add()
    #list of all employees
print("\nList of employees in the department:")
dep.list_employee()
    



        