package lesson19;

public class Item {
    private int myId;
    private int myInv;

    public Item(int id, int inv) {
        myId = id;
        myInv = inv;
    }

    public int getId() {
        return myId;
    }

    public int getInv() {
        return myInv;
    }

    public int compareTo(Item other) {
        return 0;
    }

    public boolean equals(Item other) {
        return false;
    }

    public String toString() {
        return "";
    }

}
