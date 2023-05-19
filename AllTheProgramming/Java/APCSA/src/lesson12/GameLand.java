package lesson12;

public class GameLand {
    public static void playGameLand() {
        int[] player = { 0, 0 };
        Boolean gameEnd = false;
        while (!gameEnd) {
            next: for (int num = 0; num < 2; num++) {
                int roll = ((int) (Math.random() * 5 + Math.random() * 5 + 2));
                switch (roll) {
                    case 12:
                    case 2:
                        continue next;

                    case 7:
                        player[num] -= 7;
                        if (player[num] < 0) {
                            player[num] = 0;
                        }
                        break;
                    default:
                        player[num] += roll;
                        if (num == 0 && player[0] == player[1]) {
                            player[1] = 0;
                        } else if (num == 1 && player[0] == player[1]) {
                            player[0] = 0;
                        } else if (player[num] > 99) {
                            player[num] = 99;
                            gameEnd = true;
                        }
                        break;

                }
                for (int i = 0; i < 100; i++) {
                    if (player[0] == i) {
                        System.out.print("1");
                    } else if (player[1] == i) {
                        System.out.print("2");
                    } else {
                        System.out.print("_");
                    }
                }
                System.out.println("");
            }
        }
    }

    public static void main(String[] args) {
        playGameLand();
    }
}
