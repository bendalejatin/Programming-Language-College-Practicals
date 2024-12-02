/*  PRACTICAL-2: Write a program for calculator.

Name: Jatin Bendale
Enrollment No.: 202203103510038
Branch: B.Tech CSE 
*/

// CODE:

import java.util.Scanner;
public class practical2{
    public static void main(String[]args){
        Scanner obj = new Scanner(System.in);
        double num1,num2;

        System.out.println("Enter the two numbers:");

        num1 = obj.nextDouble();
        num2 = obj.nextDouble();

        System.out.println("Enter the operation (+,-,*,/,%)");
        
        char op = obj.next().charAt(0);
        double result =0;

        switch(op){
            case '+':
                result= num1 +num2;
                break;
            
            case '-':
                result= num1 -num2;
                break;

            case '*':
                result= num1 *num2;
                break;

            case '/':
                result= num1 /num2;
                break;

            case '%':
                result= num1 %num2;
                break;  
            default:
                System.out.println("ERROR !!!");
        }
        System.out.println("The Result of operation ("+ op +") is :"+ result);
    }
}