package lesson7;

public class Grocerys {

    public static void calulate(float i1, float i2, float i3, float i4, float i5) {
        System.out.printf("%-10s%-10s%s\n", "Item:", "Cost:", "Total:");
        float total = i1;
        System.out.printf("%-10s%-10.2f%.2f\n", "#1", i1, total);
        total += i2;
        System.out.printf("%-10s%-10.2f%.2f\n", "#2", i2, total);
        total += i3;
        System.out.printf("%-10s%-10.2f%.2f\n", "#3", i3, total);
        total += i4;
        System.out.printf("%-10s%-10.2f%.2f\n", "#4", i4, total);
        total += i5;
        System.out.printf("%-10s%-10.2f%.2f", "#5", i5, total);

    }
}