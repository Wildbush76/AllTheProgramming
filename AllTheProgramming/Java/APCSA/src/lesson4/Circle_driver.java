package lesson4;

import java.util.Scanner;

public class Circle_driver {
    public static void main(String[] args) {
        Scanner what = new Scanner(System.in);
        System.out.println("what is da X");
        double x = what.nextDouble();
        System.out.println("What is da Y");
        double y = what.nextDouble();
        System.out.println("What is da radius");
        double radius = what.nextDouble();
        Circle yes = new Circle(x, y, radius);
        yes.draw();
        System.out.println("The circumference is " + yes.circumference());
        System.out.println("The area is " + yes.area());
        what.close();
    }
}