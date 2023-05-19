package lesson12;

import gpdraw.*;
import java.awt.Color;

public class Pictures {
    private static DrawingTool yea = new DrawingTool(new SketchPad(500, 500, 0));

    public static void makeTable(int d1, int d2) {
        System.out.print("     ");
        for (int i = 1; i <= d2; i++) {
            System.out.printf("%5d", i);
        }
        System.out.print("\n");
        for (int y = 1; y <= d2; y++) {
            System.out.printf("\n%5d", y);
            for (int x = 1; x <= d1; x++) {
                System.out.printf("%5d", y * x);
            }
        }
    }

    public static void pyramid(int size) {
        for (int i = 0; i < size; i++) {
            System.out.println(" ".repeat(size - i - 1) + "*".repeat(i * 2 + 1));
        }
    }

    public static void circle() {
        yea.setWidth(5);
        for (int i = 0; i < 360; i++) {
            yea.setColor(
                    new Color((int) (Math.random() * 255), (int) (Math.random() * 255), (int) (Math.random() * 255)));
            yea.forward(250);
            yea.backward(250);
            yea.turnRight(1);
        }
    }
}
