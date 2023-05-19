package lesson9;

public class Fibonacci {
    public int Fib(int n) {
        if (n == 0 || n == 1)
            return 1;
        return Fib(n - 1) + Fib(n - 2);

    }

    public int multi(int num1, int num2) {
        if (num1 == 1)
            return num2;
        return num2 + multi(num1 - 1, num2);
    }

    public static void main(String[] args) {
        Fibonacci yea = new Fibonacci();
        System.out.println(yea.multi(5, 3));
    }
}
