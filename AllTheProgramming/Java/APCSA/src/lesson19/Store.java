package lesson19;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Store {
    private ArrayList<Item> myStore = new ArrayList<Item>();

    public Store(String fName) {
        loadFile(fName);
    }

    public Store() {
    }

    private void loadFile(String inFileName) {
        try {
            File file = new File(inFileName);
            Scanner looker = new Scanner(file);
            while (looker.hasNextLine()) {
                int id = looker.nextInt();
                int count = looker.nextInt();
                myStore.add(new Item(id, count));
            }
            looker.close();
        } catch (FileNotFoundException fnf) {
            System.out.println("looks like your missing a file");
        }
    }

    public void displayStore() {
    }

    public String toString() {
        return "this is a string";
    }

    public void Sort() {
    } // to get recursive sort going

    private void merge(ArrayList<Item> a, int start, int mid, int stop) {
        int size = stop - start;
        int pos1 = start;
        int pos2 = mid + 1;
        Item[] temp = new Item[size];
        for (int index = 0; index < size; index++) {
            if (pos1 < mid && pos2 <= stop) {
                if (a.get(pos1).compareTo(a.get(pos2)) < 0) {
                    temp[index] = a.get(pos1++);
                } else {
                    temp[index] = a.get(pos2++);
                }
            } else if (pos1 < mid + 1) {
                temp[index] = a.get(pos1++);
            } else {
                temp[index] = a.get(pos2++);
            }
        }
        for (Item i : temp) {
            a.set(start++, i);
        }
    }

    public void mergeSort(ArrayList<Item> a, int first, int last) {
        if (last - first <= 2) {
            swap(a, first, last);
        } else {
            int mid = (first + last) / 2;
            mergeSort(a, first, mid);
            mergeSort(a, mid + 1, last);
            merge(a, first, mid, last);
        }
    }

    private void swap(ArrayList<Item> list, int a, int b) {
        if (b - a < 2) {
            return;
        }
        Item temp = list.get(a);
        if (list.get(a).compareTo(list.get(b)) < 0) {
            list.set(a, list.get(b));
        } else {
            list.set(b, temp);
        }
    }
}
