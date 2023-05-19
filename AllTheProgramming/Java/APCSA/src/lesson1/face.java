package lesson1;

import gpdraw.*;

public class face {
    public static void main(String[] args) {
        SketchPad poster = new SketchPad(600, 600);
        DrawingTool marker = new DrawingTool(poster);
        for (int x = 0; x < 4; x++) {
            marker.forward(200);

            marker.turnRight(90);
        }
        marker.up();
        marker.move(40, 60);
        marker.down();
        marker.move(40, 30);
        marker.move(160, 30);
        marker.move(160, 60);
        marker.up();
        marker.move(60, 150);
        marker.down();
        marker.drawCircle(10);
        marker.up();
        marker.move(140, 150);
        marker.down();
        marker.drawCircle(10);
        marker.up();
        marker.move(100, 100);
        marker.down();
        marker.move(80, 80);
        marker.move(100, 80);

    }
}
