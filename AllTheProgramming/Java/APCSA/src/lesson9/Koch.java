package lesson9;

import gpdraw.*;

public class Koch {
    private DrawingTool pencil;
    private SketchPad paper;

    private int nums;
    private int length;

    public void makeIt() {
        for (int i = 0; i < 3; i++) {
            drawIt(nums, length);
            pencil.turnRight(120);
        }
    }

    public Koch(int n, int l) {
        paper = new SketchPad(500, 500, 1);
        pencil = new DrawingTool(paper);
        pencil.up();

        pencil.turnLeft(180);
        pencil.forward((Math.sqrt(3) * l / 2.0) * (2 / 3.0));

        pencil.turnRight(180);

        pencil.turn(30);
        pencil.down();
        nums = n;
        length = l;

    }

    private void drawIt(int nums, double length) {
        if (nums < 1) {
            pencil.forward(length);
        } else {
            drawIt(nums - 1, length / 3);
            pencil.turnLeft(60);
            drawIt(nums - 1, length / 3);
            pencil.turnRight(120);
            drawIt(nums - 1, length / 3);
            pencil.turnLeft(60);
            drawIt(nums - 1, length / 3);
        }
    }

    public static void main(String[] args) {
        Koch yes = new Koch(7, 300);
        yes.makeIt();

    }
}
