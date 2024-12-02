/*practical-15:Write a program that executes two threads. One thread displays
               “Thread1”every 2,000 milliseconds, and the other displays
               “Thread2” every 4,000 milliseconds.Create the threads by
               extending the Thread class.
*/
//CODE:

class Thread1 extends Thread {
    public void run() {
        int n = 1;
        while (n < 10) {
            System.out.println("Thread1");
            try {
                Thread.sleep(2000);
            } catch (Exception e) {
                System.out.println("Exception: " + e.getMessage());
            } finally {
                n++;
            }
        }
    }
}

class Thread2 extends Thread {
    public void run() {
        int n = 1;
        while (n < 10) {
            System.out.println("Thread2");
            try {
                Thread.sleep(4000);
            } catch (Exception e) {
                System.out.println("Exception: " + e.getMessage());
            } finally {
                n++;
            }
        }
    }
}

class practical15 {
    public static void main(String[] args) {
        Thread1 t1 = new Thread1();
        Thread2 t2 = new Thread2();
        t1.start();
        t2.start();
    }
}
