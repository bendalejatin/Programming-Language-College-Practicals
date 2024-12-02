/*  PRACTICAL-4: Write a program to print inputs given from command line
                 arguments on the console.
*/
// CODE:

public class practical4{
    public static void main(String[]args){
        for(int i=0;i<args.length;i++){
            System.out.println("This command line input is " +args[i]);
        }
    }
}
