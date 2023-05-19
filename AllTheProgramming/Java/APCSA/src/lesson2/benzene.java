/* 
 * Created By Henry Kirk
 * A program to create the symbol for benzene, which is made of a hexagon and circle
 */
package lesson2;

import gpdraw.*;

public class benzene {
    private SketchPad poster;
    private DrawingTool marker;

    public benzene() {
        poster = new SketchPad(600, 600, 0);
        marker = new DrawingTool(poster);
    }

    public void draw() {
        marker.up();
        marker.forward(200);
        marker.turnLeft(120);
        marker.down();
        double why = Math.abs(Math.sin(30) * 200);
        for (int x = 0; x < 6; x++) {
            marker.forward(why);
            marker.turnLeft(60);
        }
        marker.up();
        marker.home();
        marker.down();
        marker.drawCircle(150);
    }

    public static void main(String[] args) {
        benzene yes = new benzene();
        yes.draw();
    }
}
