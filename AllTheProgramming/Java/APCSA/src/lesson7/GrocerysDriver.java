package lesson7;

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class GrocerysDriver {
    public static void main(String[] args) throws FileNotFoundException {
        float pricey[] = { 0, 0, 0, 0, 0 };

        System.out.println("Wanna read from a file (1 yes, 0 no)");
        Scanner looky = new Scanner(System.in);
        if (looky.nextInt() == 1) {
            File words = new File("C:\\Users\\kirkh\\Desktop\\input.txt");
            looky.close();
            looky = new Scanner(words);
            for (int x = 1; x < 6; x++) {
                pricey[x - 1] = looky.nextFloat();
            }

        } else {

            for (int x = 1; x < 6; x++) {
                System.out.printf("Enter item #%s: ", x);
                pricey[x - 1] = looky.nextFloat();
            }
        }
        System.out.println("");
        Grocerys.calulate(pricey[0], pricey[1], pricey[2], pricey[3], pricey[4]);
        looky.close();
    }
}
