package lesson13;

public class CheckingAccount {
    private double myBalance;
    // private int myAccountNumber;

    public CheckingAccount() {
        myBalance = 0.0;
        // myAccountNumber = 0;
    }

    public CheckingAccount(double initialBalance, int acctNum) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Your balance can't be negative");
        }
        myBalance = initialBalance;
        // myAccountNumber = acctNum;
    }

    public double getBalance() {

        return myBalance;
    }

    public void deposit(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("You can't deposit negative amounts");
        }
        myBalance += amount;
    }

    public void withdraw(double amount) {
        if (amount > myBalance) {
            throw new IllegalArgumentException("Your too poor idiot, cousin timmy never runs out of funds");
        }
        myBalance -= amount;
    }
}