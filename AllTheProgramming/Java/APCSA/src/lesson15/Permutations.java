package lesson15;

import java.util.ArrayList;

public class Permutations {
    public ArrayList<Integer> create() {
        ArrayList<Integer> choices = new ArrayList<Integer>();
        for (int i = 1; i < 11; i++) {
            choices.add(i);
        }
        ArrayList<Integer> perm = new ArrayList<Integer>();
        while (choices.size() > 0) {
            int ind = (int) (Math.random() * choices.size());
            perm.add(choices.get(ind));
            choices.remove(ind);
        }
        return perm;
    }

    public static void main(String[] args) {
        System.out.println("Random Permutation List Generator");
        Permutations yea = new Permutations();
        for (int i = 1; i < 11; i++) {
            ArrayList<Integer> ye = yea.create();
            System.out.printf("List %d: ", i);
            for (int e = 0; e < ye.size(); e++) {
                System.out.printf(" %2d", ye.get(e));
            }
            System.out.println();
        }

    }
}
