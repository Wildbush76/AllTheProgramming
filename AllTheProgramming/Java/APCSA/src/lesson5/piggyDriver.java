package lesson5;

import java.util.Scanner;

public class piggyDriver {
    public static void main(String[] args) {
        piggyBank banco;
        Scanner yes = new Scanner(System.in);
        System.out.println("do you have money yes(1) no(2)");

        if (yes.nextInt() == 1) {
            System.out.println("How many pennies?");
            int penny = yes.nextInt();
            System.out.println("How many nickels?");
            int nickel = yes.nextInt();
            System.out.println("How many dimes?");
            int dime = yes.nextInt();
            System.out.println("How many quarters?");
            int quarter = yes.nextInt();
            banco = new piggyBank(penny, nickel, dime, quarter);
        } else {
            banco = new piggyBank();
        }
        boolean running = true;
        while (running) {
            System.out.println(
                    "what you wanna do? addPennies(ap), addNickles(an), addDimes(ad), addQuarters(aq), getValues(gv), exit(exit)");
            String wat = yes.next();
            switch (wat.toLowerCase()) {
                case "ap":
                    System.out.println("How many pennies?");
                    banco.addPenny(yes.nextInt());
                    break;

                case "an":
                    System.out.print("How many nickels?");
                    banco.addNickels(yes.nextInt());
                    break;

                case "ad":
                    System.out.println("How many dimes?");
                    banco.addDimes(yes.nextInt());
                    break;
                case "aq":
                    System.out.println("How many quarters?");
                    banco.addQuarters(yes.nextInt());
                    break;
                case "gv":
                    System.out.println(
                            "What do you want to get? totalValue(tv) pennies(p) nickels(n) dimes(d) quarters(q)");
                    switch (yes.next().toLowerCase()) {
                        case "tv":
                            System.out.println("$" + banco.howRich());
                            break;
                        case "p":
                            System.out.println(banco.howManyPenny());
                            break;
                        case "n":
                            System.out.println(banco.howManyNickel());
                            break;
                        case "d":
                            System.out.println(banco.howManyDime());
                            break;
                        case "q":
                            System.out.println(banco.howManyQuarter());
                            break;
                        default:
                            System.out.print("wat?");

                    }
                    break;
                case "exit":
                    System.out.println("Bye!");
                    yes.close();
                    running = false;
                    break;
                default:
                    System.out.println("I don't know what you want to do");
                    break;
            }
        }
    }
}