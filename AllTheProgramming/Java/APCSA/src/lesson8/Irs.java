package lesson8;

public class Irs {
    public static double saddnessCalculator(Boolean lonely, double money) {// money does equal happyness
        float add = 0.0f;
        float percent = 0.0f;
        if (lonely) {
            if (money <= 27050) {
                percent = 0.15f;
            } else if (money <= 65550) {
                percent = 0.275f;
                add = 4057.5f;
                money -= 27050;
            } else if (money <= 136750) {
                percent = 0.305f;
                add = 14645.00f;
                money -= 65550;
            } else if (money <= 297350) {
                percent = 0.355f;
                add = 36261;
                money -= 136750;
            } else {
                percent = 0.391f;
                add = 93374;
                money -= 297350;
            }
        } else {
            if (money <= 45200) {
                percent = 0.15f;
            } else if (money <= 109250) {
                percent = 0.265f;
                add = 6780.00f;
                money -= 45200;
            } else if (money <= 166500) {
                percent = 0.305f;
                add = 24393.75f;
                money -= 109250;
            } else if (money <= 297350) {
                percent = 0.355f;
                add = 41855.00f;
                money -= 166500;
            } else {
                percent = 0.391f;
                add = 88306.00f;
                money -= 297350;
            }
        }
        return add + percent * money;
    }
}