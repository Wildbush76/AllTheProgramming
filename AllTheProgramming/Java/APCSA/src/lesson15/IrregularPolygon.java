package lesson15;

import gpdraw.*;
import java.util.ArrayList;
import java.awt.geom.*;

public class IrregularPolygon {
    private ArrayList<Point2D.Double> points;
    private SketchPad paper;
    private DrawingTool pencil;

    public IrregularPolygon() {
        paper = new SketchPad(500, 500, 0);
        pencil = new DrawingTool(paper);
        points = new ArrayList<Point2D.Double>();
    }

    public void addPoint(double x, double y) {
        points.add(new Point2D.Double(x, y));
    }

    public void draw() {
        for (int i = 0; i < points.size(); i++) {
            int index2 = 0;
            if (i < points.size() - 1) {
                index2 = i + 1;
            }

            double angle = Math.atan2(((Double) points.get(index2).getY() - points.get(i).getY()),
                    (points.get(index2).getX() - points.get(i).getX()));
            angle = Math.toDegrees(angle);
            pencil.setDirection(angle);
            pencil.forward(points.get(i).distance(points.get(index2)));
        }
    }

    public double calcPerimeter() {
        double total = 0;
        for (int i = 0; i < points.size(); i++) {
            int index2 = 0;
            if (i < points.size() - 1) {
                index2 = i + 1;
            }
            total += points.get(i).distance(points.get(index2));
        }
        return total;
    }

    public double calcArea() {
        double area = 0;
        for (int i = 0; i < points.size(); i++) {
            double x0 = points.get(i).getX();
            double y0 = points.get(i).getY();

            double x1;
            double y1;
            if (i < points.size() - 1) {
                x1 = points.get(i + 1).getX();
                y1 = points.get(i + 1).getY();
            } else {
                x1 = points.get(0).getX();
                y1 = points.get(0).getY();
            }
            area += x0 * y1 - x1 * y0;
        }
        return Math.abs(area / 2.0);
    }
}