/*practical-12:Write a program in Java to demonstrate implementation of multiple
inheritance using interfaces.

Name:Jatin Bendale
Enrollment no.:202203103510038
Branch:B.tech CSE*/

//CODE:

interface face1 {
    void method1();
}

interface face2 {
    void method2();
}

class sub implements face1, face2 {
    public void method1() {
        System.out.println("Hello");
    }

    public void method2() {
        System.out.println("Amtics !!!");
    }
}

public class practical12 {
    public static void main(String args[]) {
        sub ob1 = new sub();
        ob1.method1();
        ob1.method2();
    }
}