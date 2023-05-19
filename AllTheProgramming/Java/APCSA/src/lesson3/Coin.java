package lesson3;

public class Coin {
    private int Quarter;
    private int Dime;
    private int Nickel;
    private int c;

    public Coin(int change) {
        c = change;
        Quarter = 25;
        Dime = 10;
        Nickel = 5;
    }

    public void Calculate() {
        System.out.println(c + " cents =>");
        int Q = c / Quarter;
        c %= Quarter;
        int D = c / Dime;
        c %= Dime;
        int N = c / Nickel;
        c %= Nickel;
        System.out.println("Quarter(s)  " + Q);
        System.out.println("Dime(s)     " + D);
        System.out.println("Nickel(s)   " + N);
        System.out.println("Penny(s)    " + c);
    }
}
