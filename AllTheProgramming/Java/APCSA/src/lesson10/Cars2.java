package lesson10;

public class Cars2 {
    public static String Huh(String plate) {
        plate = plate.replace(" ", "");
        int one = Integer.parseInt(plate.substring(3));
        for (int i = 0; i < 3; i++) {
            one += plate.charAt(i);
        }
        char letter = (char) ('A' + one % 26);
        return letter + Integer.toString(one);
    }
}
