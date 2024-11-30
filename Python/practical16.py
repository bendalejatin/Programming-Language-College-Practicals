#Practical : 16- Write a python program to demonstrate the use of data hiding.

#class datahandling
class DataHiding:
    def __init__(self):
        self.__hidden_var = 0

    def add(self, increment):
        self.__hidden_var += increment
        print("After adding, the hidden variable is:", self.__hidden_var)

# Create an object of the DataHiding class
my_object = DataHiding()

# Call the add method and pass 5 as the increment value
my_object.add(5)

# Try to access the private variable from outside the class
print(my_object.__hidden_var)
