package lesson4;

import java.util.Scanner;

public class Rectangle_driver {
    public static void main(String[] args) {
        Scanner what = new Scanner(System.in);
        System.out.println("what is da X");
        double x = what.nextDouble();
        System.out.println("What is da Y");
        double y = what.nextDouble();
        System.out.println("What is da width");
        double width = what.nextDouble();
        System.out.println("What is da height");
        double height = what.nextDouble();
        Rectangle rectA = new Rectangle(x, y, width, height);
        rectA.draw();
        System.out.println("The perimeter is " + rectA.getPerimeter());
        System.out.println("The area is  " + rectA.getArea());
        what.close();
    }
}
