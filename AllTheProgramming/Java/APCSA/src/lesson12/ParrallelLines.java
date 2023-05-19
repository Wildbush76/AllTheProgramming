package lesson12;

import gpdraw.*;

public class ParrallelLines {
    private static DrawingTool pen = new DrawingTool(new SketchPad(700, 800, 0));

    private static void rect(double tx, double ty, double w, double h) {
        pen.up();
        pen.move(tx + (w / 2.0), ty - (h / 2.0));
        pen.down();
        System.out.println(pen.getXPos() + " " + pen.getYPos());
        // pen.fillCircle(5);
        pen.fillRect(w, h);
        // System.out.printf("yea1 %.2f yea 2 %.2f\n", tx, ty);

    }

    public static void draw() {
        for (int row = 0; row < 8; row++) {
            double offset = -0.5 * Math.cos(row * Math.PI * (1.0 / 2)) + 0.5;
            pen.up();
            pen.move(-350, -row * 100 + 400);
            pen.down();
            pen.move(350, -row * 100 + 400);

            for (int col = 0; col < 7; col += 2) {
                rect((col * 100 + offset * 50) - 350, (-row * 100) + 400, 100, 100);
            }

        }
    }

    public static void main(String[] args) {
        draw();

    }
}
