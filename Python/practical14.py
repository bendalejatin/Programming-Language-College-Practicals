#Practical : 14- Write a python program to demonstrate the use of method overriding.

#class vehicle
class Vehicle:
    def vehicle_name(self):
        print("mode of vehicle")

#class train
class Train(Vehicle):
    def vehicle_name(self):
        print("On Land")

#class aeroplane
class Aeroplane(Vehicle):
    def vehicle_name(self):
        print("In Air")

#objects
vehicle = Vehicle()
train = Train()
aeroplane = Aeroplane()

#display of objects
vehicle.vehicle_name()
train.vehicle_name()
aeroplane.vehicle_name()
