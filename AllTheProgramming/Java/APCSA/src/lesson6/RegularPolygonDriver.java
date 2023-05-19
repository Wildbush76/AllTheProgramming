package lesson6;

import java.util.Scanner;

public class RegularPolygonDriver {
    public static void main(String[] args) {

        Scanner tellMe = new Scanner(System.in);
        System.out.println("How many sides?");
        int sides = tellMe.nextInt();
        System.out.println("what is the side length");
        double length = tellMe.nextDouble();
        RegularPolygon poly = new RegularPolygon(sides, length);
        poly.draw();
        System.out.println("sides = " + poly.getNumside());
        System.out.println("length = " + poly.getSideLength());
        System.out.printf("theta = %.2f\n", poly.vertexAngle());
        System.out.printf("r = %.2f\n", poly.getr());
        System.out.printf("R = %.2f\n", poly.getR());
        System.out.printf("Perimeter = %.2f\n", poly.Perimeter());
        System.out.printf("Area = %.2f", poly.Area());
        tellMe.close();
    }
}