package lesson4;

import gpdraw.*;
import java.lang.Math;

public class Sphere {
    private SketchPad poster;
    private DrawingTool pencil;

    private void drawLine(double x1, double y1, double x2, double y2) {
        pencil.up();
        pencil.move(x1, y1);
        pencil.down();
        pencil.move(x2, y2);
    }

    public Sphere() {
        poster = new SketchPad(600, 600, 0);
        pencil = new DrawingTool(poster);

    }

    public void draw() {
        int M = 100;
        int N = 100;
        for (int m = 0; m <= M; m++) {
            double prevx = 0.0;
            double prevy = 0.0;
            for (int n = 0; n <= N; n++) {
                double x = Math.sin(Math.PI * m / M) * Math.cos(2 * Math.PI * n / N) * 100;
                double y = Math.sin(Math.PI * m / M) * Math.sin(2 * Math.PI * n / N) * 100;
                double z = Math.cos(Math.PI * m / M) * 100;
                y = z;

                if (n > 0) {
                    drawLine(prevx, prevy, x, y);
                }
                prevx = x;
                prevy = y;
            }
        }

        for (int n = 0; n <= N; n++) {
            double prevx = 0.0;
            double prevy = 0.0;
            for (int m = 0; m <= M; m++) {
                double x = Math.sin(Math.PI * m / M) * Math.cos(2 * Math.PI * n / N) * 100;
                double y = Math.sin(Math.PI * m / M) * Math.sin(2 * Math.PI * n / N) * 100;
                double z = Math.cos(Math.PI * m / M) * 100;

                y = z;
                if (n > 0) {
                    drawLine(prevx, prevy, x, y);
                }
                prevx = x;
                prevy = y;
            }
        }

    }

}
