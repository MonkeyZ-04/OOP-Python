# name , salary

class Employee: #build class

    def __init__(self,name,salary,department): #Start Method 
        self.name = name
        self.salary = salary
        self.department = department

    #Build Method

    def showData(self):
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))
        print(f"Department : {self.department}")

    def __del__(self):
        print("Call Destructor")
        # จิงๆไม่ต้องระบุก็ได้ Method นี้เป็นการเครียแรม คืนค่าหน่วยความจำให้ระบบ

# Build object
# Employee() call  Constructor
obj1 = Employee("Non",50000,"Accounting")
obj1.salary = 70000 # Change Attribute
obj1.showData()

obj2 = Employee("Mon",120,"Duck")
obj2.salary = "Zon"
obj2.showData()

obj3 = Employee("Nono",100000,"Ceo")
obj3.showData()