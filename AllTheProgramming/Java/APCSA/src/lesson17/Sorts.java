package lesson17;

import java.util.*;

public class Sorts {
    private long steps;

    public Sorts() {
        steps = 0;
    }

    public void bubbleSort(ArrayList<Comparable> list) {
        // replace these lines with your code
        for (int outer = 0; outer < list.size() - 1; outer++) {
            for (int inner = 0; inner < list.size() - outer - 1; inner++) {
                steps += 3;
                if (list.get(inner).compareTo(list.get(inner + 1)) > 0) {
                    // swap list[inner] & list[inner+1]
                    Comparable temp = list.get(inner);
                    list.set(inner, list.get(inner + 1));
                    list.set(inner + 1, temp);
                    steps += 4;
                }
            }
        }
        System.out.println();
        System.out.println("Bubble Sort");
        System.out.println();
    }

    public void selectionSort(ArrayList<Comparable> list) {
        int min;
        Comparable temp;
        for (int outer = 0; outer < list.size() - 1; outer++) {
            steps++;
            min = outer;
            for (int inner = outer + 1; inner < list.size(); inner++) {
                steps += 3;
                if (list.get(inner).compareTo(list.get(min)) < 0) {
                    min = inner; // a new smallest item is found
                }

            }
            // swap list[outer] & list[min]
            temp = list.get(outer);
            list.set(outer, list.get(min));
            list.set(min, temp);
            steps += 4;
        }

        // replace these lines with your code
        System.out.println();
        System.out.println("Selection Sort");
        System.out.println();
    }

    public void selectionSort(ArrayList<Comparable> list, int start, int stop) {
        int min;
        Comparable temp;
        for (int outer = start; outer <= stop; outer++) {
            min = outer;
            for (int inner = outer + 1; inner < stop + 1; inner++) {
                steps += 3;
                if (list.get(inner).compareTo(list.get(min)) < 0) {
                    min = inner;
                }
            }
            // swap list[outer] & list[min]
            temp = list.get(outer);
            list.set(outer, list.get(min));
            list.set(min, temp);
            steps += 4;
        }

    }

    void quickSort(ArrayList<Comparable> list, int first, int last) {
        int g = first, h = last;
        int midIndex = (first + last) / 2;
        Comparable dividingValue = list.get(midIndex);
        steps++;
        do {
            while (list.get(g).compareTo(dividingValue) < 0) {
                g++;
                steps += 2;
            }
            while (list.get(h).compareTo(dividingValue) > 0) {
                h--;
                steps += 2;
            }
            if (g <= h) {
                // swap(list[g], list[h]);
                swap(list, g, h);
                g++;
                h--;
            }
        } while (g < h);
        if (h > first)
            quickSort(list, first, h);
        if (g < last)
            quickSort(list, g, last);
    }

    public void insertionSort(ArrayList<Comparable> list) {
        for (int outer = 1; outer < list.size(); outer++) {
            int position = outer;
            Comparable key = list.get(position);
            steps++;
            // Shift larger values to the right

            while (position > 0 && list.get(position - 1).compareTo(key) > 0) {
                list.set(position, list.get(position - 1));
                steps += 4;
                position--;
            }

            list.set(position, key);
            steps++;
        }
    }

    private void merge(ArrayList<Comparable> a, int start, int mid, int stop) {
        // replace these lines with your code
        int size = stop - start;
        int pos1 = start;
        int pos2 = mid + 1;
        // ArrayList<Comparable> temp = new ArrayList<Comparable>(size);
        Comparable[] temp = new Comparable[size];

        for (int index = 0; index < size; index++) {
            if (pos1 < mid && pos2 <= stop) {
                if (a.get(pos1).compareTo(a.get(pos2)) < 0) {
                    temp[index] = a.get(pos1++);
                } else {
                    temp[index] = a.get(pos2++);
                }
                steps += 4;
            } else if (pos1 < mid + 1) {
                temp[index] = a.get(pos1++);
                steps++;
            } else {
                temp[index] = a.get(pos2++);
                steps++;
            }
        }
        for (Comparable i : temp) {
            a.set(start++, i);
            steps++;
        }
        // life is insufferable

    }

    void mergeSort(ArrayList<Comparable> numbers, int first, int last) {
        if (last - first <= 2) {
            selectionSort(numbers, first, last);
        } else {
            int mid = (first + last) / 2;
            mergeSort(numbers, first, mid);
            mergeSort(numbers, mid + 1, last);
            merge(numbers, first, mid, last);
        }
    }

    public void badMergeSort(ArrayList<Comparable> values) {
        int mid = values.size() / 2;
        selectionSort(values, 0, mid);
        selectionSort(values, mid + 1, values.size() - 1);
        merge(values, 0, mid, values.size() - 1);
    }

    public long getStepCount() {
        return steps;
    }

    public void setStepCount(long stepCount) {
        steps = stepCount;
    }

    public void swap(ArrayList<Comparable> list, int a, int b) {
        // replace these lines with your code
        Comparable temp = list.get(a);
        list.set(a, list.get(b));
        list.set(b, temp);
        steps += 4;
    }
}
