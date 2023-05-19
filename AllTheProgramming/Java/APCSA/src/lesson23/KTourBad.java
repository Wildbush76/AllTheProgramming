package lesson23;

public class KTourBad {
    private int[][] board;

    private int playerX;
    private int playerY;

    private int[][] moves = { { 1, 2, 2, 1, -1, -2, -2, -1 }, { -2, -1, 1, 2, 2, 1, -1, -2 } };// your stupid

    public KTourBad() {
        board = new int[8][8];
        playerX = 0;
        playerX = 0;
        board[0][0] = 0;
    }

    private boolean isThisMoveStupid(int dx, int dy) {
        if (playerX + dx < 0 || playerX + dx > board.length - 1 || playerY + dy < 0
                || playerY + dy > board.length - 1) {
            return false;
        }
        return true;
    }

    private boolean canWeEvenMove() {
        for (int move = 0; move < 8; move++) {
            if (isThisMoveStupid(moves[0][move], moves[1][move])
                    && board[playerY + moves[1][move]][playerX + moves[0][move]] == 0) {
                return true;
            }
        }
        return false;
    }

    public void display() {
        for (int[] y : board) {
            for (int x : y) {
                System.out.printf("%-3d|", x);
            }

            System.out.print("\n" + "-".repeat(32) + "\n");
        }
    }

    public void howFarCanWeGoWithoutBeingReallyStupid() {
        int count = 1;
        while (count < 64) {
            int num = (int) (Math.random() * 8);
            if (!isThisMoveStupid(moves[0][num], moves[1][num])
                    || board[playerY + moves[1][num]][playerX + moves[0][num]] != 0) {
                continue;
            }
            board[playerY][playerX] = count++;
            playerX += moves[0][num];
            playerY += moves[1][num];
            board[playerY][playerX] = count;
            if (!canWeEvenMove()) {
                System.out.println("we tried and we cried but at last we were not good enough");
                System.out.println("but atleast we got to " + (count));
                display();
                break;
            }
        }
    }

    public static void main(String[] args) {
        KTourBad haha = new KTourBad();
        haha.howFarCanWeGoWithoutBeingReallyStupid();
    }
}
