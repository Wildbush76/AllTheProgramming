package lesson10;

public class CaesarSalad {
    private static final int[] VALUES = { 1, 5, 10, 50, 100, 500, 1000 };
    private static final String LETTERS = "IVXLCDM";

    public static int Roman2num(String haha) {
        if (!romanChecker(haha)) {
            System.out.println("Your stuff is wrong");
            return -1;
        }
        int total = 0;
        for (int i = 0; i < haha.length() - 1; i++) {
            int here = VALUES[LETTERS.indexOf(haha.charAt(i))];
            total += (here >= VALUES[LETTERS.indexOf(haha.charAt(i + 1))]) ? here : -here;
        }
        return total + VALUES[LETTERS.indexOf(haha.charAt(haha.length() - 1))];
    }

    private static boolean romanChecker(String yes) {
        for (int i = 0; i < yes.length() - 1; i++) {
            int here = VALUES[LETTERS.indexOf(yes.charAt(i))];
            if (here < VALUES[LETTERS.indexOf(yes.charAt(i + 1))]) {
                if (VALUES[LETTERS.indexOf(yes.charAt(i + 1))] / (double) here != 5
                        && VALUES[LETTERS.indexOf(yes.charAt(i + 1))] / (double) here != 10) {
                    return false;
                }
            }
        }
        return !yes.matches("[^MDCLXVI]*|.*I{4,}.*|.*V{4,}.*|.*X{4,}.*|.*L{4,}.*|.*C{4,}.*|.*D{4,}.*|.*M{4,}.*");
    }

    public static String Num2Roman(int yes) {
        String[] vals = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int[] vals2 = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };

        int pos = 0;
        String romen = "";
        while (yes > 0) {
            if (yes / vals2[pos] == 0) {
                pos++;
                continue;
            }
            romen += vals[pos];
            yes -= vals2[pos];
        }
        if (!romanChecker(romen)) {
            System.out.println(romen);
            System.out.println("something aint right, i can feel it");
            return "your wrong";
        }
        return romen;
    }
}
