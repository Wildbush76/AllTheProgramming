package lesson2;

import gpdraw.*;

public class circles2 {
    private SketchPad poster;;
    private DrawingTool marker;

    public circles2() {
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
        marker.up();
        marker.move(0, 60);
        marker.down();
        marker.drawCircle(60);
        marker.drawString("Middle");

    }

    public static void main(String[] args) {
        circles2 yes = new circles2();
        yes.draw();
    }
}
