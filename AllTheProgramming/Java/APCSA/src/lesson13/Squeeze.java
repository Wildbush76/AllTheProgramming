package lesson13;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Squeeze {
    private static Scanner look;
    private static File file;

    public static void SqueezeFile(String dir) {
        try {
            file = new File(dir);
            look = new Scanner(file);
        } catch (FileNotFoundException fnfe) {
            System.out.println("File was not found");
            return;
        }
        while (look.hasNextLine()) {
            String line = look.nextLine();
            int count = 0;
            while (line.charAt(count) == ' ') {
                count++;
            }
            line = line.substring(count);
            System.out.printf("%d %s\n", count, line);
        }
    }

    public static void main(String[] args) {
        SqueezeFile("C:/Users/kirkh/Downloads/squeeze.txt");
    }
}
