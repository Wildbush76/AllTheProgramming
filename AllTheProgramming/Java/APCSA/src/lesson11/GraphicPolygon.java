package lesson11;

import lesson6.RegularPolygon;

public class GraphicPolygon extends RegularPolygon {
    private double xPos, yPos;

    public GraphicPolygon(int numberOfSides, double sideLength) {
        super(numberOfSides, sideLength);
        xPos = 0;
        yPos = 0;
    }

    public GraphicPolygon(int numberOfSides, double sideLength, double x, double y) {
        super(numberOfSides, sideLength);
        xPos = x;
        yPos = y;
    }

    public void moveTo(double newX, double newY) {
        xPos = newX;
        yPos = newY;
    }

    public void draw() {
        pen.up();
        pen.move(xPos, yPos);
        super.draw();
    }
}
