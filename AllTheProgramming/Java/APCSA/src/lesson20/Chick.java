package lesson20;

public class Chick implements Animal {
    private String myType;
    private String mySound;
    private String mySound2;
    private boolean twoNoises;

    Chick() {
        myType = "chick";
        mySound = "cheep";
        twoNoises = false;
    }

    Chick(boolean secondSound) {
        myType = "chick";
        mySound2 = "cluck";
        mySound = "cheep";
        twoNoises = secondSound;
    }

    public String getSound() {
        if (twoNoises) {
            if (Math.floor(Math.random() * 2) == 1) {
                return mySound;
            } else {
                return mySound2;
            }
        } else {
            return mySound;
        }
    }

    public String getType() {
        return myType;
    }
}
