package lesson15;

import java.util.Scanner;

public class IrregularPolygonDriver {
    public static void main(String[] args) {
        IrregularPolygon haha = new IrregularPolygon();
        Scanner looking = new Scanner(System.in);
        boolean selecting = true;
        int pointsAdd = 0;
        while (selecting) {
            System.out.println("Type X and Y seprated by a comma, type done when done");
            String weeee = looking.nextLine();
            if (weeee.toLowerCase().equals("done")) {
                if (pointsAdd < 3) {
                    System.out.println("You stupid idiot that's not a polygon");
                }
                break;
            }
            String[] temp = weeee.split(",");
            haha.addPoint(Double.parseDouble(temp[0]), Double.parseDouble(temp[1]));
            pointsAdd++;
        }
        haha.draw();
        System.out.printf("Perimeter : %.2f\n", haha.calcPerimeter());
        System.out.printf("Area : %.2f", haha.calcArea());
        looking.close();
    }
}