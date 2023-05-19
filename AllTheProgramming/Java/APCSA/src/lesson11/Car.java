package lesson11;

public class Car extends Vehicle {
    private String myCarType; // type of car
    private int myNumPassengers; // number of passengers
    private int myNumDoors; // number of car doors

    // constructor
    public Car(String brand, String type, int price, double mileage, double gasPrice,
            int miles, int passengers, int numDoors) {
        // uses Vehicle's constructor
        super(brand, price, mileage, gasPrice, miles);

        // initializes what's new to Car
        myCarType = type;
        myNumPassengers = passengers;
        myNumDoors = numDoors;
    }

    public String getCarType() {
        return myCarType;
    }

    public int getNumPassengers() {
        return myNumPassengers;
    }

    public int getNumDoors() {
        return myNumDoors;
    }

    // overloads toString() method
    public String toString() {
        return "Your $" + getPrice() + " " + getBrand() + " "
                + myCarType + " costs " + formatter.format("$%.2f", getYearlyMiles()
                        / getGasMileage() * getGasPrice())
                + " in gas each year!\nIt has " + myNumDoors + " doors and carries "
                + myNumPassengers + " passengers.";
    }

}
