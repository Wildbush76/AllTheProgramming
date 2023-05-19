package lesson4;

public class Car {

    private int startMiles;
    private int endMiles;
    private double gallons;

    public Car(int miles) {
        startMiles = miles;
        endMiles = miles;
        gallons = 0.0;
    }

    public void fillUp(int miles, double g) {
        endMiles = miles;
        gallons += g;
    }

    public double calculateMPG() {
        return (endMiles - startMiles) / gallons;
    }

    public void resetMPG() {
        startMiles = endMiles;
        gallons = 0;
    }
}
