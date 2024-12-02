/*  PRACTICAL-3: Write a program that reads a number in meters, converts it to feet,
                 and displays the result.
*/
// CODE:

import java.util.Scanner;

public class practical3 {
    public static void main(String[]args){
        Scanner obj = new Scanner(System.in);
        double meters , feets;
        System.out.println("Enter the number in meters:");
        meters = obj.nextDouble();

        feets = meters * 3.2808;

        System.out.println("The number in feets is: "+ feets);
    }

}
