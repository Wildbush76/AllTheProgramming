package lesson6;

import java.util.Scanner;

public class MyMathDriver {
    public static void main(String[] args) {
        Scanner badAtMath = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out
                    .println("watcha wanna do today fToC(0) cToF(1) volume(2) hypotenuse(3) roots(4) zero(5) exit(6)");
            int choice = badAtMath.nextInt();
            switch (choice) {
                case 0:
                    System.out.println("what is the tempature in F");
                    System.out.println(MyMath.fToC(badAtMath.nextDouble()));
                    break;
                case 1:
                    System.out.println("what is the tempature in C");
                    System.out.println(MyMath.cToF(badAtMath.nextDouble()));
                    break;
                case 2:
                    System.out.println("what is the radius");
                    System.out.println(MyMath.Volume(badAtMath.nextDouble()));
                    break;
                case 3:
                    System.out.println("whats the a");
                    double a = badAtMath.nextDouble();
                    System.out.println("whats the b");
                    double b = badAtMath.nextDouble();
                    System.out.println(MyMath.hypo(a, b));
                    break;
                case 4:
                    System.out.println("whats the a");
                    double aa = badAtMath.nextDouble();
                    System.out.println("whats the b");
                    double bb = badAtMath.nextDouble();
                    System.out.println("whats the c");
                    double cc = badAtMath.nextDouble();
                    double[] yes = MyMath.roots(aa, bb, cc);
                    System.out.println("root 1 " + yes[0]);
                    System.out.println("root 2 " + yes[1]);
                    break;
                case 5:
                    System.out.println(MyMath.zero());
                    break;
                case 6:
                    System.out.println(":c");
                    running = false;
                    break;

            }
        }
        System.out.println("bye bye");
        badAtMath.close();
    }
}
