//  PRACTICAL-14: Write a program in Java to demonstrate multiple try block and multiple catch exception.

// CODE:

public class practical14{
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
        } 
        catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception: Cannot divide by zero!");
        } 
        catch (Exception e) {
            System.out.println("Exception Occured");
        }
        try {
            int[] arr = { 1, 2, 3 };
            System.out.println(arr[5]);
        } 
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index Out of Bounds Exception: Invalid array index!");
        }
        try {
            String str = "abc";
            int num = Integer.parseInt(str);
        } 
        catch (NumberFormatException e) {
            System.out.println("Number Format Exception: Invalid number format!");
        }

        System.out.println("Program continues after handling exceptions.");
    }
}
