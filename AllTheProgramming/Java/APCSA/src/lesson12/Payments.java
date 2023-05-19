package lesson12;

public class Payments {
    private static int start = 0;

    private static void pay(double p, double rate, double mp, int mounth, int other) {
        double intrest = mp * p;
        if (p < rate || mounth == 0) {
            return;
        }
        double newB = (p + intrest) - (rate * other);
        int mmm = mounth;
        if (other == -1) {
            mounth = start - mounth;
        }
        System.out.printf("%-10d%-10.2f%-10.2f%-10.2f%-10.2f\n", mmm, p, intrest, rate, newB);
        pay(newB, rate, mp, mounth + other, other);
    }

    public static void payment(double p, double percent, double rate) {
        System.out.println("Month   Principal  Interest  Payment   New Balance");
        pay(p, rate, percent / 1200, 1, 1);
    }

    public static void invest(double p, double percent, double rate, int months) {
        System.out.println("Month   Principal  Interest  Investment   New Balance");
        start = months;
        pay(p, rate, percent / 1200, months, -1);

    }

}
