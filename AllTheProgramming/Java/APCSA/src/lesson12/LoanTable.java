package lesson12;

public class LoanTable {
    public static void calc(double p, double t, double li, double hi) {
        System.out.printf("Principal = $%.2f\nTime = %.2f years\nLow rate = %.2f\nHigh rate = %.2f\n\n", p, t, li,
                hi);
        System.out.println("Annual Interest Rate   Monthly Payment\n");
        for (double i = li; i <= hi; i += 0.25) {
            double k = (i / 100) / 12;
            double c = Math.pow(1 + k, t * 12);
            double a = (p * k * c) / (c - 1);
            System.out.printf("%13.2f%22.2f\n", i, a);
        }
    }
}