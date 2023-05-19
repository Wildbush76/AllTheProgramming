package lesson14;

import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

public class Compact {
    public int[] doTheThing(String directory) {
        try {
            File f = new File(directory);
            Scanner input = new Scanner(f);
            int pos = 0;
            System.out.print("Before");
            while (input.hasNext()) {
                int num = input.nextInt();
                if (num != 0) {
                    pos++;
                }
                System.out.print(" ," + num);
            }
            input.close();
            input = new Scanner(f);
            int[] values = new int[pos];
            pos = 0;
            while (input.hasNext()) {
                int num = input.nextInt();
                if (num != 0) {
                    values[pos] = num;
                    pos++;
                }
            }
            System.out.print("\nAfter");
            for (int i : values) {
                System.out.print(" ," + i);
            }
            input.close();
            return values;

        } catch (FileNotFoundException fnf) {
            System.out.println("The specified file was not found");
            return new int[0];
        }
    }

    public static void main(String[] args) {
        Compact y = new Compact();
        y.doTheThing("C:/Users/kirkh/Downloads/compact.txt");
    }
}
