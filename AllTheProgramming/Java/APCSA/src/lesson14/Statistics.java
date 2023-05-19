package lesson14;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class Statistics {
    public Statistics() {

    }

    public void doStatistics(String dir) {
        try {
            File file = new File(dir);
            Scanner scan = new Scanner(file);
            int[] values = new int[1000];
            Arrays.fill(values, -1);

            short counter = 0;
            long total = 0;
            while (scan.hasNext()) {
                short value = scan.nextShort();
                total += value;
                values[counter++] = value;
            }
            double average = (double) total / counter;
            double totalDevation = 0.0;
            for (int i = 0; i < counter; i++) {
                totalDevation += Math.pow(values[i] - average, 2);
            }
            totalDevation = Math.sqrt(totalDevation / (counter - 1));// idk its probaly it

            // mode

            System.out.printf("average : %.2f \nstandardDevation : %.2f\n", average, totalDevation);
            Arrays.sort(values);
            int maxV = values[0];
            int max = 0;
            int count = 1;
            int prev = 0;
            for (int i = 0; i < counter; i++) {
                if (values[i] == -1) {
                    continue;
                }
                if (values[i] != prev) {
                    if (count > max) {
                        max = count;
                        maxV = prev;
                    }
                    prev = values[i];
                    count = 1;
                } else {
                    count++;
                }
            }
            System.out.printf("Mode : %d", maxV);
            for (int e = 0; e < counter; e++) {
                if (values[e] == -1) {
                    continue;
                }
                if (values[e] != prev) {
                    if (count == max && prev != maxV) {
                        System.out.printf(" , %d", prev);
                    }
                    count = 1;
                    prev = values[e];
                } else {
                    count++;
                }
            }

            scan.close();
        } catch (FileNotFoundException fnfe) {
            System.out.println("The specifed file was not found");
        }

    }

    public static void main(String[] args) {
        Statistics yes = new Statistics();
        yes.doStatistics("C:/Users/kirkh/Downloads/numbers.txt");
    }
}
