package lesson10;

import java.util.Scanner;

public class CaesarDriver {
    public static void main(String[] args) {
        Scanner lolz = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("what would you like to do 1.Roman to Arabic 2. Arabic to Roman 3.exit");
            int response = lolz.nextInt();
            switch (response) {
                case 1:
                    String in = lolz.next();
                    System.out.println(in);
                    System.out.println(CaesarSalad.Roman2num(in));
                    break;
                case 2:
                    int inn = lolz.nextInt();
                    System.out.println(CaesarSalad.Num2Roman(inn));
                    break;
                case 3:
                    running = false;
                    break;
                default:
                    System.out.println("that was not an option");
                    break;
            }
        }
        lolz.close();// abcdefghijklmnopqrstuvwxyz
    }
}
