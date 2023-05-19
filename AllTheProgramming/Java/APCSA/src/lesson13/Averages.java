package lesson13;

import java.io.File;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Averages {
    private static File file;
    private static Scanner look;

    public static double getAverage(String fileName) {
        try {
            file = new File(fileName);
            look = new Scanner(file);
        } catch (FileNotFoundException nofiles) {
            System.out.println("the specifed file was not found");
            return 0;
        }
        long total = 0;
        int count = 0;
        try {
            while (look.hasNext()) {
                total += look.nextInt();
                count++;
            }
            return (double) total / count;
        } catch (ArithmeticException ae) {
            System.out.println("attemped to divide by zero, check that the file has at least one number");
        } catch (InputMismatchException ime) {
            System.out.println("An invalid character was found within the file");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return 0;

    }

    public static void main(String[] args) {
        System.out.printf("The average is %.2f", getAverage("C:/Users/kirkh/Downloads/numbers.txt"));
    }
}
