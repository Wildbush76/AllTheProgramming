package lesson8;

import java.util.Scanner;

public class IrsDriver {
    public static void main(String[] args) {
        Scanner iListen = new Scanner(System.in);
        System.out.println("How much money do you have?");
        float money = iListen.nextFloat();
        System.out.println("Are your married? true or false");
        double output = Irs.saddnessCalculator(!iListen.nextBoolean(), money);
        System.out.printf("Taxs = $%.2f", output);
        iListen.close();
    }
}
