package lesson12;

public class FunLoops {
    public static void magicSquare(int n) {
        int current = 0;
        long yes = 0;
        long numz = 1;
        long next = 1;
        while (current < n) {
            long square = numz * numz;
            while (yes < square) {
                yes += next;
                next++;
            }
            if (yes == square) {
                current++;
                System.out.println(yes);

            }
            numz++;
        }
    }

    public static int LCM(int num1, int num2) {
        int multi = 1;
        while ((num1 * multi) % num2 != 0) {
            multi++;
        }
        return num1 * multi;

    }
}