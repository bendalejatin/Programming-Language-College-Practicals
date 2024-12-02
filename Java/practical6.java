/*  PRACTICAL-6: Write a program that prompts the user to enter a letter and check
                 whether a letter is a vowel or constant.
*/
// CODE:

import java.util.Scanner ;
public class practical6 {
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the letter:");
        char ch = input.next().charAt(0);
        switch(Character.toLowerCase(ch))
        {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                System.out.println(ch +" is the vowel.");
                break;
            default:
                System.out.println(ch +" is the constant.");
        }
    }
}
