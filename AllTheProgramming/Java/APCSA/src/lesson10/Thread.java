package lesson10;

import java.util.Scanner;

public class Thread {
    public static void main(String[] args) {
        Scanner lolz = new Scanner(System.in);
        boolean using = true;

        while (using) {
            System.out.println("\n Please input a string");
            String woord = lolz.nextLine();
            System.out.println("what would you like to do ");
            System.out.print("1. reverse 2. Palindrome 3. piglatin 4. shortTalk 5. exit : ");
            switch (lolz.nextInt()) {
                case 1:
                    System.out.println(StringCheese.reversed(woord));
                    break;
                case 2:
                    System.out.println(StringCheese.Palindrome(woord));
                    break;
                case 3:
                    System.out.println(StringCheese.piggy(woord));
                    break;
                case 4:
                    System.out.println(StringCheese.shortTalk(woord));
                    break;
                case 5:
                    System.out.println("... but why....");
                    using = false;
                    break;
                default:
                    System.out.println("To unlock this feature please pay 5$ in amazon giftcards");
                    break;
            }
            lolz.next();
        }
        lolz.close();

    }
}