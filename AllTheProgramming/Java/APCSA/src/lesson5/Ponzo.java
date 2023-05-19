package lesson5;

import gpdraw.*;

public class Ponzo {
    private SketchPad paper;
    private DrawingTool pen;

    public Ponzo() {
        paper = new SketchPad(600, 600, 0);
        pen = new DrawingTool(paper);
    }

    void line(int x1, int y1, int x2, int y2) {
        pen.up();
        pen.move(x1, y1);
        pen.down();
        pen.move(x2, y2);
    }

    public void drawPonzo() {
        line(-400, 0, -400, 0);
        pen.setDirection(45);
        for (int angle = 0; angle < 11; angle++) {
            pen.forward(700);
            pen.backward(700);
            pen.turnRight(90 / 11);
        }
        pen.setWidth(4);
        line(-50, -100, -50, 100);
        line(50, -100, 50, 100);
    }
}