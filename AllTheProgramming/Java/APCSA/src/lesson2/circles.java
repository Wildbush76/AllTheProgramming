package lesson2;

import gpdraw.*;

public class circles {
    private SketchPad poster;;
    private DrawingTool marker;

    public circles() {
        poster = new SketchPad(600, 600);
        marker = new DrawingTool(poster);
    }

    public void draw() {

        marker.drawCircle(50);
        marker.drawString("Small");
        marker.up();
        marker.move(0, 120);
        marker.down();
        marker.drawCircle(70);
        marker.drawString("Big");

    }

    public static void main(String[] args) {
        circles yes = new circles();
        yes.draw();
    }
}