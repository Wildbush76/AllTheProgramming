package lesson4;

import gpdraw.*;
import java.lang.Math;

public class Circle {
    private double x;
    private double y;
    private double radius;
    private SketchPad paper;
    private DrawingTool pen;

    public Circle(double X, double Y, double rad) {
        x = X;
        y = Y;
        radius = rad;
        paper = new SketchPad(500, 500);
        pen = new DrawingTool(paper);
    }

    public void draw() {
        pen.up();
        pen.move(x, y);
        pen.down();
        pen.drawCircle(radius);
    }

    public double circumference() {
        return Math.PI * radius * 2;
    }

    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }
}
