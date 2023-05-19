package lesson6;

import java.util.Scanner;

public class TaxesDriver {
    public static void main(String[] args) {
        Scanner yep = new Scanner(System.in);
        double h = yep.nextDouble();
        double p = yep.nextDouble();
        Taxes taxEvasion = new Taxes(h, p);
        taxEvasion.value();
        yep.close();
    }
}
