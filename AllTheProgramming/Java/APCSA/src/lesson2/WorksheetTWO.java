package lesson2;

import gpdraw.*;

public class WorksheetTWO {
    private DrawingTool marker;
    private SketchPad poster;

    public WorksheetTWO() {
        poster = new SketchPad(600, 600);
        marker = new DrawingTool(poster);
    }

    public void draw() {
        marker.drawCircle(80);
        marker.up();
        marker.home();
        marker.forward(80);
        marker.down();
        marker.setDirection(0);
        marker.forward(80);
        marker.turnRight(90);
        marker.forward(160);
        marker.turnRight(90);
        marker.forward(160);
        marker.turnRight(90);
        marker.forward(160);
        marker.turnRight(90);
        marker.forward(80);
        marker.up();
        marker.home();
        marker.down();
        marker.drawCircle(113.137);

    }

    public static void main(String[] args) {
        WorksheetTWO yes = new WorksheetTWO();
        yes.draw();
    }
}
