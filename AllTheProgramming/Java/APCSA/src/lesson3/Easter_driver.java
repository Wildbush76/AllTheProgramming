package lesson3;

import java.util.Scanner;

public class Easter_driver {
    public static void main(String[] args) {
        Scanner YES = new Scanner(System.in);
        boolean userStupid = true;
        while (userStupid) {
            try {
                int yer = YES.nextInt();

                if (yer < 1583) {
                    System.out.println("Easter didnt happen the.. try again");
                } else {
                    Easter yea = new Easter(yer);
                    yea.calculate();
                    userStupid = false;
                }
            } catch (Exception e) {
                System.out.println("stop it.. bad.. don't do that");
                YES.next();
            }
        }
        YES.close();

    }
}