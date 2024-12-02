//  PRACTICAL-13: Write a program in Java to develop user defined exception for ‘Divide by Zero’ error.
    
// CODE:

class DivideByZeroException extends Exception {
    public DivideByZeroException(String message) {
        super(message);
    }
}

// Main class demonstrating the custom exception
public class practical13{
    public static void main(String[] args) {
        try{
            int numerator = 10;
            int denominator = 0;

            // Check if denominator is zero
            if(denominator == 0){
                throw new DivideByZeroException("Cannot divide by zero!");
            }

            int result = numerator/denominator;
            System.out.println("Result: " + result);
        }
        catch(DivideByZeroException e){
            System.out.println("Error: " + e.getMessage());
        }
    }
}
