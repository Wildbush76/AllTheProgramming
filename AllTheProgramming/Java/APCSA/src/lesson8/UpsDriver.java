package lesson8;

import java.util.Scanner;

public class UpsDriver {
    public static void main(String[] args) {
        double[] nope = { 0, 0, 0, 0 };
        Scanner eyes = new Scanner(System.in);
        System.out.print("What is the first dimesion ");
        nope[0] = eyes.nextDouble();
        System.out.print("What is the second dimesion ");
        nope[1] = eyes.nextDouble();
        System.out.print("What is the third dimesion ");
        nope[2] = eyes.nextDouble();
        System.out.print("What is the weight");
        nope[3] = eyes.nextDouble();
        Ups box = new Ups(nope[0], nope[1], nope[2], nope[3]);
        box.checky();
        eyes.close();
    }
}
