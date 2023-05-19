package lesson1;

import gpdraw.*;

public class housey {
    public static void rect(int yes1, int yes2, int yes3, int yes4, DrawingTool yea) {
        yea.up();
        yea.move(yes1, yes2);
        yea.down();
        yea.setDirection(0);
        for (int x = 0; x < 4; x++) {
            if (x % 2 == 0) {
                yea.forward(yes3);
            } else {
                yea.forward(yes4);
            }
            yea.turnRight(90);
        }

    }

    public static void main(String[] args) {

        SketchPad poster = new SketchPad(500, 500);
        DrawingTool marker = new DrawingTool(poster);
        rect(-200, 50, 400, 200, marker);
        rect(-40, -50, 80, 100, marker);
        marker.up();
        marker.move(-200, 50);
        marker.down();
        marker.move(0, 200);
        marker.move(200, 50);
        marker.up();
        marker.move(-20, -100);
        marker.down();
        marker.drawCircle(5);
        rect(-150, 0, 50, 50, marker);
        rect(100, 0, 50, 50, marker);

    }
}
