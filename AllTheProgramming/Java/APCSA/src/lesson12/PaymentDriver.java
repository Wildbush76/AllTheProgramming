package lesson12;

import java.util.Scanner;

public class PaymentDriver {
    public static void main(String[] args) {
        Scanner watcher = new Scanner(System.in);
        System.out.print("What's the principle ");
        double p = watcher.nextDouble();
        System.out.print("What's the yearly rate (percent) ");
        double per = watcher.nextDouble();
        System.out.print("What's the monthly payment ");
        double mp = watcher.nextDouble();
        Payments.payment(p, per, mp);
        watcher.close();
    }
}