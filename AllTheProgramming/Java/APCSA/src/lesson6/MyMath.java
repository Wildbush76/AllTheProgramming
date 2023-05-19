package lesson6;

public class MyMath {
    public static double fToC(double f) {
        return (5.0 / 9) * (f - 32);
    }

    public static double cToF(double c) {
        return c / (5.0 / 9) + 32;
    }

    public static double Volume(double radius) {
        return (4.0 / 3) * Math.PI * Math.pow(radius, 3);
    }

    public static double hypo(double a, double b) {
        return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
    }

    public static double[] roots(double a, double b, double c) {
        double rooty = (-b + Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);
        double rootx = (-b - Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);
        double[] ye = { rooty, rootx };
        return ye;
    }

    public static int zero() {
        return 0;
    }
}
