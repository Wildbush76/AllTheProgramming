package lesson12;

public class Grade {
    public static Boolean checkEligiblity(String yes) {
        yes = yes.toLowerCase();
        yes.replaceAll("\\s", "");
        double gpa = 0.0;
        boolean loser = false;
        for (int i = 0; i < yes.length(); i += 2) {
            switch (yes.charAt(i)) {
                case 'a':
                    gpa += 4;
                    break;
                case 'b':
                    gpa += 3;
                    break;
                case 'c':
                    gpa += 2;
                    break;
                case 'd':
                    gpa += 1;
                    break;
                case 'f':
                    loser = true;
                    break;
            }
        }
        gpa /= Math.ceil(yes.length() / 2.0);
        System.out.printf("GPA = %-5.2f", gpa);
        if (yes.length() < 7) {
            System.out.println("Ineligible, taking less than 4 classes");
            return false;
        }
        if (gpa < 2) {
            if (loser) {
                System.out.println("Ineligible, gpa below 2.0 and has F grade");
                return false;
            }
            System.out.println("Ineligible, gpa below 2.0");
            return false;
        } else if (loser) {
            System.out.println("Ineligible, gpa above 2.0 but has F grade");
            return false;
        }
        System.out.println("Eligible");
        return true;
    }
}
