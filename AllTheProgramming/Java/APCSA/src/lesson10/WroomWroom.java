package lesson10;

import java.util.Scanner;

public class WroomWroom {
    public static void main(String[] args) {
        Scanner scany = new Scanner(System.in);
        System.out.println("what's your car??");
        String[] make = scany.nextLine().split(" ");

        System.out.println("Whats the liceanse plate");
        String plates = scany.nextLine();
        String lightingMcQueen = Cars2.Huh(plates);
        System.out.printf("Make = %s", make[0]);
        System.out.printf("\nModel = %s", make[1]);
        System.out.printf("\n%s = %s", plates, lightingMcQueen);
        scany.close();
    }
}
