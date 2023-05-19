public class SpiralMatrix {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        if (n == 1) {
            matrix[0][0] = 1;
            return matrix;
        }
        short current = 1;
        byte x = 0;
        byte y = 0;
        byte delta = 1;

        for (int shell = 0; shell < n - 1; shell++) {
            for (int i = 0; i < 2; i++) {
                for (; (delta == 1 && x < n - shell - 1) || (delta == -1 && x > shell); x += delta) {
                    matrix[y][x] = current++;
                }
                for (; (delta == 1 && y < n - shell) || (delta == -1 && y > shell); y += delta) {

                    matrix[y][x] = current++;
                }
                y -= delta;
                x -= delta;
                delta *= -1;
            }
        }

        return matrix;
    }

    public static void main(String[] args) {
        SpiralMatrix test = new SpiralMatrix();
        test.generateMatrix(5);
    }
}