package lesson20;

public class NamedCow extends Cow {
    private String myName;

    public NamedCow(String name) {
        myName = name;
    }

    public String getName() {
        return myName;
    }
}
