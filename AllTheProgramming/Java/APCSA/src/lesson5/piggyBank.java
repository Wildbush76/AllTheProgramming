package lesson5;

public class piggyBank {
    private int pennies;
    private int nickels;
    private int dimes;
    private int quarters;

    public piggyBank() {
        pennies = 0;
        nickels = 0;
        dimes = 0;
        quarters = 0;
    }

    public piggyBank(int penny, int nickel, int dime, int quarter) {
        pennies = penny;
        nickels = nickel;
        dimes = dime;
        quarter = quarters;

    }

    int howManyPenny() {
        return pennies;
    }

    int howManyNickel() {
        return nickels;
    }

    int howManyDime() {
        return dimes;
    }

    int howManyQuarter() {
        return quarters;
    }

    void addPenny(int penny) {
        pennies += penny;
    }

    void addNickels(int nickel) {
        nickels += nickel;
    }

    void addDimes(int dime) {
        dimes += dime;
    }

    void addQuarters(int quarter) {
        quarters += quarter;
    }

    void addMoney(int penny, int nickel, int dime, int quarter) {
        pennies += penny;
        nickel += nickels;
        dimes += dime;
        quarters += quarter;
    }

    public double howRich() {
        return ((double) pennies + nickels * 5 + dimes * 10 + quarters * 25) / 100;
    }
}