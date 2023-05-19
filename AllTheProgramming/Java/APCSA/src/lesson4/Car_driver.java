package lesson4;

import java.util.Scanner;

public class Car_driver {
    public static void main(String[] args) {
        Scanner yea = new Scanner(System.in);
        System.out.println("What's the odometer reading");
        int reading = yea.nextInt();
        Car auto = new Car(reading);
        System.out.print("New car odometer readings " + reading);
        auto.fillUp(150, 8);
        System.out.println("Miles per gallon" + auto.calculateMPG());
        System.out.println("Miles per gallon" + auto.calculateMPG());
        auto.resetMPG();
        auto.fillUp(350, 10);
        auto.fillUp(450, 20);
        System.out.println("Miles per gallon" + auto.calculateMPG());
        auto.resetMPG();
        auto.fillUp(603, 25.5);
        System.out.print("Miles per gallon" + auto.calculateMPG());
        yea.close();
    }
}
