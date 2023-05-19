package lesson19;

public class BondMain {

    public static void main(String[] args) {
        BondMovieSeries seriesData = new BondMovieSeries("C:/Users/kirkh/Downloads/bond.txt");
        seriesData.sort();
        seriesData.displayInfo();
    }

}
