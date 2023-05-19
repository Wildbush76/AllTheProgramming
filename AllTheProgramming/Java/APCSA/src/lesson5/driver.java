package lesson5;

class Methods {
    public Methods() {
    }

    public int north(int num1, int num2) {
        int temp = num1;
        num1 = num2;
        num2 = temp;
        System.out.println("num1 - num2 = " + (num1 - num2));
        return (3 * (num1 - num2));
    }

    public double south(double num3, double num4) {
        num3 += 24;
        num4 *= 2;
        System.out.println("num3 / num4 = " + (num3 / num4));
        return (10 * (num3 + num4));
    }

}

public class driver {
    public static void main(String[] args) {
        Methods app = new Methods();
        int a = 40, b = 25;
        double c = 13, d = -2;
        System.out.println("To start, a - b = " + (a - b));
        int hello = app.north(a, b);
        System.out.println("Now, a - b = " + (a - b));
        System.out.println("north returned " + hello);
        System.out.println("c / d = " + c / d);
        double goodbye = app.south(c, d);
        System.out.println("Now, c / d = " + c / d);
        System.out.println("south returned " + goodbye);
    }
}
