# Match the following inheritance types with real-life examples:
"""   a) Single Inheritance
      b) Multiple Inheritance
      c) Multilevel Inheritance
      d) Hierarchical Inheritance   """

# a) Single Inheritance      
print("   Single Inheritance: ")  # single parent single child
class Car:    # class 
    def color(self):  # method
        print("The color of the car is Black.")
 
class BMW(Car):   #  drive class from Car
    def model(self):
        print("The model of the car is BMW x5.")

car = BMW()
car.color()
car.model()

print()

# b) Multiple Inheritance
print("   Multiple Inheritance:")  # one child two parents
class SoftwareDeveloper:
    def task(self):
        print("They handle all tasks in development field.")

class ProjectLead:
    def manage(self):
        print("They manage the project relate resources.")

class TechLead(SoftwareDeveloper, ProjectLead):
    def execute(self):
        print("They handle or execute project.")

company = TechLead()
company.task()
company.manage()
company.execute()

print()

# c) Multilevel Inheritance
print("   Multilevel Inheritance:")  # same like a family chain 
class Company:
    def company_info(self):
        print("Name of Company: ABC Tech Company.")

class Department(Company):
    def department_info(self):
        print("This is one department of ABC Tech Compny: Software Development.")

class Team(Department):
    def team_info(self):
        print("This team works for backend development.")

comp = Team()
comp.company_info()
comp.department_info()
comp.team_info()

print()

#  d) Hierarchical Inheritance 
print("   Hierarchical Inheritance: ")  # one parent many children 

class Department:
    def info(self):
        print("This is main brach of differnt department.")

class ProjectManager(Department):
    def role(self): 
        print("This is one part of department.")

class Developer(Department):
    def work(self):
        print("This is another part of department.")

project = ProjectManager()
project.info()
project.role()



dev = Developer()
dev.info()
dev.work()

