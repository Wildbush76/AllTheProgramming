package lesson11;

public class SportsCar extends Car {
    private String color;
    private int liters;
    private String suspension;
    private String tires;

    public SportsCar(String brand, String type, int price, double mileage, double gasPrice, int miles, int passengers,
            int numDoors, String myColor, int MyEngine, String mySuspension, String myTires) {
        super(brand, type, price, mileage, gasPrice, miles, passengers, numDoors);
        color = myColor;
        liters = MyEngine;
        suspension = mySuspension;
        tires = myTires;
    }

    public String toString() {
        return super.toString() + "\nYour cool " + color + " sports car has a " + liters + " liter engine, "
                + suspension + " suspension and " + tires + " tires.";
    }

}
