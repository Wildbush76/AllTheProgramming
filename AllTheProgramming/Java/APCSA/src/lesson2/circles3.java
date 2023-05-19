package lesson2;

import gpdraw.*;

public class circles3 {
    private SketchPad poster;;
    private DrawingTool marker;

    public circles3() {
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
        marker.turnLeft(90);
        marker.up();
        for (int x = 3; x < 6; x++) {
            int distance = 70 + x * 10;
            marker.forward(distance);
            marker.down();
            marker.drawCircle(x * 10);
            switch (x) {
                case 3:
                    marker.drawString("Left");
                    break;
                case 4:
                    marker.drawString("Above");
                    break;
                case 5:
                    marker.drawString("Right");
                    break;
            }
            marker.up();
            marker.backward(distance);
            marker.turnRight(90);
        }

    }

    public static void main(String[] args) {
        circles3 yes = new circles3();
        yes.draw();
    }
}
