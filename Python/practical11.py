#Practical : 11- Create a class named employee having attributes - emp_name, emp_age, and 
# emp_city. Create a method named get_data() in employee class that takes user 
# input for these attributes. Derive a class named emp_derived() from the employee 
# class, having an __init__() method that displays the attributes of the employee 
# class upon instantiation.

#class emoloyee
class employee(): 
    #class attributes
    def __init__(self): 
        self.emp_name = None 
        self.emp_age = None 
        self.emp_city = None
    
    #method for taking input of above attributes
    def get_data(self): 
        self.emp_name = input("Employee Name:") 
        self.emp_age = input("Employee's Age:") 
        self.emp_city = input("Employee's City:")

#derived class
class emp_derived(employee): 
    def __init__(self): 
        employee.get_data(self) 
        print("\n###Employee Details###\n") 
        print("Name of Employee:" ,self.emp_name) 
        print("Age of Employee:" ,self.emp_age) 
        print("City of Employee:" ,self.emp_city)

#display of class
emp_derived() 
