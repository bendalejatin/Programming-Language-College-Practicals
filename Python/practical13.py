#Practical : 13- Write a python program to create a class named area. Define a class method 
# find_area() that can find areas of different shapes whose value is given by the 
# user. Invoke the class method by instantiation and prove method overloading.

#class Area  
class Area :
    @classmethod
    def find_area(cls, length=None, width=None, radius=None , height=None ,base=None ):
        if width is not None :
            return length*width
        elif radius is not None :
            return 3.14*(radius ** 2)
        elif length is not None :
            return length*length
        elif height is not None :
            return 0.5*base*height
        else :
            return None

print("\nArea of Differnt Shapes\n")

#rectangle area
rectangle_area= Area.find_area(10,20)
print("Rectangle Area :", rectangle_area)

#Square area
square_area=Area.find_area(length=10)
print("Square Area: ", square_area)

#Circle area
circle_area=Area.find_area(radius=10)
print("Circle Area: ", circle_area)

#triangle area
triangle_area=Area.find_area(height=15,base=15)
print("triangle Area: ", triangle_area)
