/*  PRACTICAL-7:Assume a vehicle plate number consists of three uppercase letters
                followed by four digits. Write a program to generate a plate number.
*/
// CODE:

public class practical7 {
    public static void main(String[] args) {
        int letter1 = 'A' + (int)(Math.random() * ('Z' - 'A'));
        int letter2 = 'A' + (int)(Math.random() * ('Z' - 'A'));
        int letter3 = 'A' + (int)(Math.random() * ('Z' - 'A'));

        int digit1 = (int)(Math.random() * 10);
        int digit2 = (int)(Math.random() * 10);
        int digit3 = (int)(Math.random() * 10);
        int digit4 = (int)(Math.random() * 10);

        System.out.println("Generated Plate Number: " + (char)(letter1) + ((char)(letter2)) +((char)(letter3)) + digit1 + digit2 + digit3 + digit4);
    }
}
