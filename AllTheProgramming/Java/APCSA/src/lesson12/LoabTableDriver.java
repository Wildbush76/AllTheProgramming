package lesson12;

import java.util.Scanner;

public class LoabTableDriver {
    public static void main(String[] args) {

        Scanner scanz = new Scanner(System.in);

        System.out.println("What is the principle");
        double p = scanz.nextDouble();
        System.out.println("What is the time in years");
        double t = scanz.nextDouble();
        System.out.println("What is the low rate (percent)");
        double li = scanz.nextDouble();
        System.out.println("What is the high rate (percent)");
        double hi = scanz.nextDouble();
        LoanTable.calc(p, t, li, hi);
        scanz.close();
    }
}
