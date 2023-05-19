package lesson6;

public class Taxes {
    private double hours;
    private double pay;
    private double gross;
    private double net;
    private double fTaxed;
    private double fica;
    private double state;
    private final double FTAX = 0.154;
    private final double FICA = 0.0775;
    private final double STATETAX = 0.04;

    public Taxes(double h, double p) {// Man i love taxes
        hours = h;
        pay = p;
        gross = h * p;
        fTaxed = gross * FTAX;
        fica = gross * FICA;
        state = gross * STATETAX;
        net = gross - (fTaxed + fica + state);

    }

    public void value() {
        System.out.println("Hours worked: " + hours);
        System.out.println("Hourly rate: " + pay);
        System.out.println("\nGross pay: " + gross);
        System.out.println("Federal Tax (" + FTAX * 100 + "%): " + fTaxed);
        System.out.println("FICA Tax (" + FICA * 100 + "%): " + fica);
        System.out.println("State Tax (" + STATETAX * 100 + "%): " + state);
        System.out.println("\nNet pay: " + net);

    }
}
