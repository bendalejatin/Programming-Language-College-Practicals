/*PRACTICAL-10:Write an application that illustrates method overriding in the same
               package and different packages.
*/

// CODE(method overriding in the SAME PACKAGE):

// same_package is the folder/package in which vehicle and aeroplane packages are defined.
// all files vehicle.java, aeroplane.java and main.java are in the same folder same_package.

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
