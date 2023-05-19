package lesson3;

import java.util.Scanner;

public class Coin_driver {
    public static void main(String[] args) {
        boolean userStupid = true;
        Scanner YES = new Scanner(System.in);
        while (userStupid) {
            String co = YES.next();

            int coins = Integer.parseInt(co);
            if (coins >= 0) {
                Coin con = new Coin(coins);
                con.Calculate();
                userStupid = false;
            } else {
                System.out.println("Man, you got the negative money!?!?");
                System.out.println("alright try again, no negative money glitch allowed here");
                YES.next();
            }
        }
        YES.close();
    }
}