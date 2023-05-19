package lesson8;

public class Ups {
    private double length;
    private double girth;
    private double weight;

    public Ups(double dim1, double dim2, double dim3, double w) {
        length = Math.max(Math.max(dim1, dim2), dim3);
        girth = 2 * (dim1 + dim2 + dim3) - length * 2;
        weight = w;
    }

    public void checky() {
        if (length + girth > 100 && weight > 70) {
            System.out.println("Package is too large and heavy");
        } else if (length + girth > 100) {
            System.out.println("Package is too large");
        } else if (weight > 70) {
            System.out.println("Package is too heavy");
        } else {
            System.out.println("Package is acceptable");
        }

    }
}
