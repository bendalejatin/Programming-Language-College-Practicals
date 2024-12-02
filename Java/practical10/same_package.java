/*PRACTICAL-10:Write an application that illustrates method overriding in the same
               package and different packages.

Name: Jatin Bendale
Enrollment No.: 202203103510038
Branch: B.Tech CSE 
*/

// CODE(method overriding in the SAME PACKAGE):

//package vehicle
package same_package;

public class Vehicle{
    public void show(){
        System.out.println("In the Vehicle Class.");
    }
}

//package aerooplane
package same_package;

public class Aeroplane extends Vehicle {
    @Override
    public void show(){
        System.out.println("In the Sky.");
    }
}

//main file 
package same_package;

public class Main {
    public static void main(String[] args){
        Vehicle vehicle = new Vehicle();
        vehicle.show();

        Aeroplane aeroplane = new Aeroplane();
        aeroplane.show();
    }
}