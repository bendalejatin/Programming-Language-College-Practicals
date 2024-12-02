/*  PRACTICAL-8:Write a test program that prompts the user to enter ten numbers,
                invoke a method to reverse the numbers, display the numbers.
*/
// CODE:

import java.util.Scanner;
public class practical8 {
    public static void reverse(int num[]) {
        int j = 0, temp;
        while (j <= num.length / 2) {
          temp = num[j];
          num[j] = num[num.length - 1 - j];
          num[num.length - 1 - j] = temp;
          j++;
        }
    }
    public static void main(String[] args) {
        int i = 0;
        int num_array[] = new int[5];
        Scanner in = new Scanner(System.in);
        for (i = 0; i < 5; i++) {
          System.out.print("Enter at Number " + (i + 1) + " : ");
          num_array[i] = in.nextInt();
        }
        reverse(num_array);
        System.out.println("After reversing numbers in an Array :");
        for (i = 0; i < 5; i++) {
          System.out.println("Value at Number " + (i + 1) + " : " + num_array[i]);
        }
    }
}
