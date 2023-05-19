package lesson6;

import gpdraw.*;

public class RegularPolygon {

    private int myNumSides; // # of sides
    private double mySideLength; // length of side
    private double myR; // radius of circumscribed circle
    private double myr; // radius of inscribed circle
    protected SketchPad paper;
    protected DrawingTool pen;

    // constructors
    public RegularPolygon() {
        myNumSides = 3;
        mySideLength = 5;
        calcR();
        calcr();
    }

    public RegularPolygon(int numSides, double sideLength) {
        myNumSides = numSides;
        mySideLength = sideLength;
        calcR();
        calcr();
        paper = new SketchPad(500, 500, 0);
        pen = new DrawingTool(paper);
    }

    // private methods
    private void calcr() {
        myr = (1.0 / 2) * mySideLength * (1 / Math.tan(Math.PI / myNumSides));
    }

    private void calcR() {
        myR = (1.0 / 2) * mySideLength * (1 / Math.sin(Math.PI / myNumSides));
    }

    // public methods
    public void draw() {
        double cx = pen.getXPos();
        double cy = pen.getYPos();
        pen.up();
        pen.backward(myR);
        pen.turnRight(90);
        pen.forward(mySideLength / 2);
        double theta = 180 - vertexAngle();
        pen.down();
        for (int i = 0; i < myNumSides; i++) {
            pen.turnLeft(theta);
            pen.forward(mySideLength);
        }
        pen.up();
        pen.move(cx, cy);
        pen.down();

        pen.drawCircle(myR);
        pen.drawCircle(myr);
    }

    public double vertexAngle() {
        return ((double) (myNumSides - 2) / myNumSides) * 180;
    }

    public double Perimeter() {
        return mySideLength * myNumSides;
    }

    public double Area() {
        return (1.0 / 2) * myNumSides * Math.pow(myR, 2) * Math.sin((2 * Math.PI) / myNumSides);
    }

    public double getNumside() {
        return myNumSides;
    }

    public double getSideLength() {
        return mySideLength;
    }

    public double getR() {
        return myR;
    }

    public double getr() {
        return myr;
    }
}