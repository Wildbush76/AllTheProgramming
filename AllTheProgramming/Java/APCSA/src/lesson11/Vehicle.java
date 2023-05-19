package lesson11;

import java.util.Formatter;

public class Vehicle {
    private String myBrand; // brand name
    private int myPrice; // price of vehicle
    private double myGasMileage; // vehicle's gas mileage
    private double myGasPrice; // gas price per gallon
    private int myYearlyMiles; // miles driven per year
    Formatter formatter = new Formatter();

    // constructor
    public Vehicle(String brand, int price, double mileage,
            double gasPrice, int miles) {
        myBrand = brand;
        myPrice = price;
        myGasMileage = mileage;
        myGasPrice = gasPrice;
        myYearlyMiles = miles;
    }

    public String getBrand() {
        return myBrand;
    }

    public int getPrice() {
        return myPrice;
    }

    public double getGasMileage() {
        return myGasMileage;
    }

    public double getGasPrice() {
        return myGasPrice;
    }

    public int getYearlyMiles() {
        return myYearlyMiles;
    }

    public String toString() {
        return "Your $" + myPrice + " " + myBrand + " costs "
                + formatter.format("$%.2f", myYearlyMiles / myGasMileage * myGasPrice)
                + " in gas each year!";
    }
}