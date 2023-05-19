package lesson15;

import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;

public class Statistics {
    private Scanner looky;
    private File file;
    private ArrayList<Integer> nums;

    public Statistics(String dir) {
        file = new File(dir);
        try {
            looky = new Scanner(file);
            nums = new ArrayList<Integer>();
            while (looky.hasNext()) {
                nums.add(looky.nextInt());
            }
        } catch (FileNotFoundException fnfe) {
            System.out.println("the file was in fact not found");
        }
    }

    public double getAverage() {
        long total = 0;
        int i;
        for (i = 0; i < nums.size(); i++) {
            total += nums.get(i);
        }

        return (double) total / i;
    }

    public double getStandardDeviation() {
        double average = getAverage();
        double standardDeviation = 0.0;
        int i;
        for (i = 0; i < nums.size(); i++) {
            standardDeviation += Math.pow(average - nums.get(i), 2);
        }
        standardDeviation /= i - 1;
        return Math.sqrt(standardDeviation);
    }

    public ArrayList<Integer> getMode() {
        ArrayList<Integer> modes = new ArrayList<Integer>();
        Collections.sort(nums);
        int[] most = { 0, 0 };
        int[] continonus = { 0, 0 };
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) == continonus[0]) {
                continonus[1]++;
            } else {
                if (continonus[1] > most[1]) {
                    most[0] = continonus[0];
                    most[1] = continonus[1];
                }
                continonus[0] = nums.get(i);
                continonus[1] = 0;
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) == continonus[0]) {
                continonus[1]++;
            } else {

                if (continonus[1] == most[1]) {
                    modes.add(continonus[0]);
                }
                continonus[0] = nums.get(i);
                continonus[1] = 0;
            }
        }
        return modes;
    }

    public static void main(String[] args) {
        Statistics hehe = new Statistics("C:/Users/kirkh/Downloads/atleast2Numbers.txt");
        System.out.printf("Average %.2f\n", hehe.getAverage());
        System.out.printf("Standard Deviation %.2f\n", hehe.getStandardDeviation());
        System.out.printf("modes %s", hehe.getMode().toString());
    }
}
