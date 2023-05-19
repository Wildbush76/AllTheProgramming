package lesson23;

import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class ConwaysGameOfLIfe {
    private short[][] grid;
    private Scanner scan;
    private int[] size;

    public ConwaysGameOfLIfe(String dir, int xSize, int ySize) {
        size = new int[2];
        size[0] = xSize;
        size[1] = ySize;
        grid = new short[size[0]][size[1]];
        Create(dir);
    }

    public ConwaysGameOfLIfe(String dir) {
        size = new int[2];
        size[0] = 20;
        size[1] = 20;
        grid = new short[size[0]][size[1]];
        Create(dir);
    }

    private void Create(String dir) {
        try {
            File file = new File(dir);
            scan = new Scanner(file);
        } catch (FileNotFoundException FNFE) {
            System.out.println("Directory not found");
            return;
        }
        for (int i = scan.nextInt(); i > 0; i--) {
            int y = scan.nextInt() - 1;
            int x = scan.nextInt() - 1;
            grid[y][x] = 1;
        }
        scan.close();
    }

    private int getNeighbors(int y, int x) {
        int total = 0;
        if (y > 0) {
            if (grid[y - 1][x] > 0) {
                total++;
            }
            if (x > 0 && grid[y - 1][x - 1] > 0) {
                total++;
            }
            if (x < size[0] - 1 && grid[y - 1][x + 1] > 0) {
                total++;
            }
        }
        if (y < size[1] - 1) {
            if (grid[y + 1][x] > 0) {
                total++;
            }
            if (x > 0 && grid[y + 1][x - 1] > 0) {
                total++;
            }
            if (x < size[0] - 1 && grid[y + 1][x + 1] > 0) {
                total++;
            }
        }
        if (x > 0 && grid[y][x - 1] > 0) {
            total++;
        }
        if (x < size[0] - 1 && grid[y][x + 1] > 0) {
            total++;
        }
        return total;
    }

    public void step() {
        for (int y = 0; y < 20; y++) {
            for (int x = 0; x < 20; x++) {
                int neighbors = getNeighbors(y, x);
                switch (neighbors) {
                    case 3:
                        if (grid[y][x] == 0) {
                            grid[y][x] = -1;
                        }
                        break;// -1 = going to be alive 0 = currently dead 1= currently alive 2= going to die
                    case 4:
                    case 5:
                    case 6:
                    case 7:
                    case 8:
                    case 0:
                    case 1:
                        if (grid[y][x] != 0)
                            grid[y][x] = 2;
                        break;
                }
            }
        }
        for (int y = 0; y < 20; y++) {
            for (int x = 0; x < 20; x++) {
                if (grid[y][x] == 2) {
                    grid[y][x] = 0;
                } else if (grid[y][x] == -1) {
                    grid[y][x] = 1;
                }
            }
        }
    }

    public void display() {
        for (short[] y : grid) {
            for (short x : y) {
                if (x != 0) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        System.out.println("-".repeat(size[0]));
    }

    public int getCountTotal() {
        int total = 0;
        for (short[] y : grid) {
            for (short x : y) {
                if (x == 1) {
                    total++;
                }
            }
        }
        return total;
    }

    public int getCountRow(int row) {
        if (row < 1 || row > 20) {
            System.out.println("Invalid row!");
            return 0;
        }
        int total = 0;
        for (int x = 0; x < 20; x++) {
            if (grid[row - 1][x] == 1) {
                total++;
            }
        }
        return total;
    }

    public int getCountColumn(int column) {
        if (column < 1 || column > 20) {
            System.out.println("Invalid row!");
            return 0;
        }
        int total = 0;
        for (int y = 0; y < 20; y++) {
            if (grid[y][column - 1] == 1) {
                total++;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        ConwaysGameOfLIfe yea = new ConwaysGameOfLIfe("C:/Users/kirkh/Downloads/life100.txt");

        for (int i = 0; i < 5; i++) {
            yea.display();
            yea.step();
        }
        yea.display();
        System.out.printf("Number in row 10 ---> %d\n", yea.getCountRow(10));
        System.out.printf("Number in column 10 ---> %d\n", yea.getCountColumn(10));
        System.out.printf("Number of living organisms ---> %d\n", yea.getCountTotal());
    }
}