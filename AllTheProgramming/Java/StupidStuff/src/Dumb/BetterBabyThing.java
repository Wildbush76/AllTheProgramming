package Dumb;

import java.util.Scanner;

public class BetterBabyThing {
    private static final Double j = 4184000000000000d;
    private static final Double c = Math.pow(299792458, 2);

    private static Double getEnergy(int babyCount) {
        double energy = (babyCount * 8.9) * c;
        return energy;
    }

    public static Double getYeildFromBaby(int babyCount) {// megatons
        Double energy = getEnergy(babyCount);
        return energy / j;
    }

    public static Double getCaloricValue(int babyCount) {
        return getYeildFromBaby(babyCount) * 1000000000000l;
    }

    public static void main(String[] args) {
        Scanner scanningYourBalls = new Scanner(System.in);
        System.out.print("enter a baby amount please : ");
        int number = scanningYourBalls.nextInt();
        System.out.printf("%.3f Megatons\n\n", getYeildFromBaby(number));
        System.out.printf("%.3f Jouls\n\n", getEnergy(number));
        System.out.printf("%.3f Calories", getCaloricValue(number));
        scanningYourBalls.close();
    }

}