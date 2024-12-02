/*  PRACTICAL-11:Describe abstract class called Shape which has three subclasses
                say Triangle, Rectangle, Circle. Define one method area() in the 
                abstract class and override this area() in these three subclasses 
                to calculate for specific object i.e. area() of Triangle subclass 
                should calculate area of triangle etc. Same for Rectangle and Circle.

Name: Jatin Bendale
Enrollment No.: 202203103510038
Branch: B.Tech CSE 
*/

// CODE:

abstract class Shape {
    double dim1;
    double dim2;    
    Shape(double a, double b) {
        dim1 = a;
        dim2 = b;
    }    
    abstract double area();
}
    
class Rectangle extends Shape {
    Rectangle(double a, double b) {
        super(a, b);
    }   
    double area() {
        System.out.println("Inside Area for Rectangle.");
        return dim1 * dim2;
    }
}
    
class Triangle extends Shape {
    Triangle(double a, double b) {
        super(a, b);
    }
    double area() {
        System.out.println("Inside Area for Triangle");
        return dim1 * dim2 / 2;
    }
}
    
class Circle extends Shape {
    Circle(double a, double b) {
        super(a, b);
    }
    double area() {
        System.out.println("Inside Area for Circle");
        return dim1 * dim2 * dim2;
    }
}
    
public class practical11 {
    public static void main(String args[]) {
        Rectangle r = new Rectangle(10, 20);
        Triangle t = new Triangle(100, 200);
        Circle c = new Circle(3.14, 15);
        Shape ref;
        ref = t;
        System.out.println("Area Of Triangle is :" + ref.area()+"\n");
        ref = r;
        ref.area();
        System.out.println("Area of Rectangle is :" + ref.area()+"\n");
        ref = c;
        ref.area();
        System.out.println("Area of Circle is : " + ref.area()+"\n");
    }
}