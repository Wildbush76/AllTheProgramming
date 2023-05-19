package lesson4;

import gpdraw.*;

public class Rectangle {
    private double myX;
    private double myY;
    private double myWidth;
    private double myHeight;

    // private DrawingTool pen;
    // private SketchPad paper;
    private static DrawingTool pen = new DrawingTool(new SketchPad(500, 500, 0));

    public Rectangle(double x, double y, double width, double height) {
        myX = x;
        myY = y;
        myWidth = width;
        myHeight = height;
        // paper = new SketchPad(500, 500, 0);
        // pen = new DrawingTool(paper);
    }

    public double getPerimeter() {
        return myHeight * 2 + myWidth * 2;
    }

    public double getArea() {
        return myWidth * myHeight;
    }

    public void draw() {
        pen.up();
        pen.move(myX, myY);
        pen.down();
        pen.setDirection(0);
        pen.forward(myWidth);
        pen.turnRight(90);
        pen.forward(myHeight);
        pen.turnRight(90);
        pen.forward(myWidth);
        pen.turnRight(90);
        pen.forward(myHeight);
        pen.turnRight(90);
    }

}