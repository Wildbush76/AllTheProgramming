package lesson5;
import gpdraw.*;
public class Muller {
    private SketchPad paper;
    private DrawingTool pen;
    public Muller() {
        paper = new SketchPad(600, 600, 0);
        pen = new DrawingTool(paper);
    }
    void drawArrow(int x, int y, int dir) {
        for (int i = 1; i > -2; i -= 2) {
            line(x * i, y, x * i - dir * i, y + dir / 3 * i);
            line(x * i, y, x * i - dir * i, y - dir / 3 * i);
        }
    }
    void line(int x1, int y1, int x2, int y2) {
        pen.up();
        pen.move(x1, y1);
        pen.down();
        pen.move(x2, y2);
    }
    void drawMuller() {
        line(-100, 0, 100, 0);
        drawArrow(-100, 0, -20);
        line(-100, -50, 100, -50);
        drawArrow(-100, -50, 20);
        line(-100, 0, -100, -50);
        line(100, 0, 100, -50);
    }
}