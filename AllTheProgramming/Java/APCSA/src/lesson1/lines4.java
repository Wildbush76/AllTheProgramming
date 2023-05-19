package lesson1;

import gpdraw.*;

public class lines4 {
    public static void main(String[] args) {
        SketchPad poster = new SketchPad(600, 600);
        DrawingTool marker = new DrawingTool(poster);
        marker.forward(120);
        marker.turnRight(45);
        marker.forward(80);
        marker.turnLeft(90);
        marker.forward(80);
        marker.turnLeft(90);
        marker.forward(80);
        marker.turnLeft(90);
        marker.forward(80);

    }
}
