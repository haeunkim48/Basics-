# Real Life Example :

# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??

# # Ans :  just make subclass from  teacher so that student will become teacher


class teacher:
    def teachers_action(self):
        print ('I teach')

class Engineer: 
    def engineers_action(self):
        print ('I code')

class youtuber:
    def youtubers_action(self):
        print ('I film')

class person (teacher, Engineer, youtuber):
    pass 

coder = person()
coder.teachers_action()
coder.engineers_action()
coder.youtubers_action()

# Design a class hierarchy with inheritance between Employee, Manager, and Intern. Implement multiple inheritance to handle the relations between these classes.

# Q. If we have an Intern who becomes a Manager, how would you handle this situation using multiple inheritance?

# Ans: Create a class that inherits from both Manager and Intern to represent an intern who becomes a manager.

# Now, if we have an Employee who is both a Manager and an Intern, then what?

# Ans: Use multiple inheritance to create a class that inherits from Employee, Manager, and Intern to represent an employee who is both a manager and an intern.

class Employee: 
    def __init__ (self, name, employee_id):
        self.name = name 
        self.employee_id = employee_id
    def display_info(self):
            print (f'Name : {self.name}')

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    
    def display_info(self):
        super().display_info()
        print (f'Deparment :{self.department}')

class Intern (Employee):
    def __init__(self, name, employee_id, supervisor):
        super().__init__ (name, employee_id)
        self.supervisor = supervisor 
    
    def display_info(self):
        super().display_info()
        print (f'Supervisor :{self.supervisor}')    

