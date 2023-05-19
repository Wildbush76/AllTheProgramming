package lesson20;

public class Pig implements Animal {
    private String myType;
    private String mySound;

    Pig() {
        mySound = "oink";
        myType = "pig";
    }

    public String getSound() {
        return mySound;
    }

    public String getType() {
        return myType;
    }
}
