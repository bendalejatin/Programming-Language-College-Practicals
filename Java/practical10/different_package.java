// CODE(method overriding in the DIFFERENT PACKAGE):

//package vehicle
package different_package.vehicle;

public class Vehicle{
    public void show(){
        System.out.println("In the Vehicle Class.");
    }
}

//package aeroplane
package different_package.aeroplane;
import different_package.vehicle.Vehicle;

public class Aeroplane extends Vehicle {
    @Override
    public void show(){
        System.out.println("In the Sky.");
    }
}

//main file
package different_package;
import different_package.vehicle.Vehicle;
import different_package.aeroplane.Aeroplane;

public class Main {
    public static void main(String[] args){
        Vehicle vehicle = new Vehicle();
        vehicle.show();

        Aeroplane aeroplane = new Aeroplane();
        aeroplane.show();
    }
}