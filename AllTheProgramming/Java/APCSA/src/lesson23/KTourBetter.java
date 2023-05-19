package lesson23;

import java.lang.Math;
import java.io.File;
import java.util.Scanner;

public class KTourBetter {
    static int theBoardInQuestion[][] = new int[8][8];
    static int accessibleBoard[][] = new int[8][8];
    static int xMoves[] = { 1, 2, 2, 1, -1, -2, -2, -1 };
    static int yMoves[] = { -2, -1, 1, 2, 2, 1, -1, -2 };

    private static int[] pushInt(int[] arr, int x) {
        int theNewOne[] = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) {
            theNewOne[i] = arr[i];
        }
        theNewOne[arr.length] = x; // goofy
        return theNewOne;
    }

    private static int[] availableMoves(int x, int y) {
        int schmovement[] = new int[0];
        for (int i = 0; i < 8; i++) {
            int movedX = x + xMoves[i];
            int movedY = y + yMoves[i];
            if (movedX >= 0 && movedX <= 7 && movedY >= 0 && movedY <= 7 && theBoardInQuestion[movedY][movedX] == 0) {
                schmovement = pushInt(schmovement, i); // yeah
            }
        }
        return schmovement;
    }

    public static void main(String[] args) {
        int move = 1;
        int position[] = { 0, 0 };
        theBoardInQuestion[0][0] = move;
        File access = new File("access.txt");
        Scanner scanning = null;
        try {
            scanning = new Scanner(access);

        } catch (Exception e) {

        }
        for (int y = 0; y < 8; y++) {
            for (int x = 0; x < 8; x++) {
                accessibleBoard[y][x] = scanning.nextInt();
            }
        }
        scanning.close();
        while (true) { // break do be do waa do be
            int schmove[] = availableMoves(position[0], position[1]);
            if (schmove.length == 0) {
                break;
            } else {
                int lowest[] = { 10, 0 }; // {amount of moves from that position, index}
                for (int i = 0; i < schmove.length; i++) {
                    int goofX = position[0] + xMoves[schmove[i]];
                    int goofY = position[1] + yMoves[schmove[i]];
                    accessibleBoard[goofY][goofX]--;

                    if (accessibleBoard[goofY][goofX] <= lowest[0]) {
                        if (accessibleBoard[goofY][goofX] == lowest[0]) {
                            if (Math.random() > 0.5) { // not proper rng; favors later on moves
                                lowest[0] = accessibleBoard[goofY][goofX];
                                lowest[1] = schmove[i];
                            }
                        } else {
                            lowest[0] = accessibleBoard[goofY][goofX];
                            lowest[1] = schmove[i];
                        }
                    }
                }
                position[0] += xMoves[lowest[1]];
                position[1] += yMoves[lowest[1]];

                move++;
                theBoardInQuestion[position[1]][position[0]] = move;
            }
        }
        for (int y = 0; y < 8; y++) {
            for (int x = 0; x < 8; x++) {
                System.out.printf("%5d", theBoardInQuestion[y][x]);
            }
            System.out.println();
        }
        System.out.println("yeah the little gueber moved " + move + " times");
    }
}
