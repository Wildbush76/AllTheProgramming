package lesson1;

import gpdraw.*;

public class lines3 {
    public static void main(String[] args) {
        SketchPad poster = new SketchPad(600, 600);
        DrawingTool marker = new DrawingTool(poster);
        marker.up();
        marker.turnRight(90);
        marker.forward(100);
        marker.down();
        marker.drawString("  A");
        marker.move(-100, 0);
        marker.up();
        marker.move(-175, 100);
        marker.down();
        marker.move(175, 100);
        marker.drawString("  B");
        marker.up();
        marker.move(0, -25);
        marker.down();
        marker.move(0, 125);
    }
}
