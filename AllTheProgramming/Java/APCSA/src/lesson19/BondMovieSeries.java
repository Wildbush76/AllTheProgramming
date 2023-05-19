package lesson19;

import java.util.*;
import java.io.*;

public class BondMovieSeries {
    private ArrayList<Movie> movieList = new ArrayList<Movie>();

    public BondMovieSeries(String fileName) {
        loadData(fileName);
    }

    private void loadData(String fileName) {
        String movieTitle;
        String bondName;
        int yearReleased;
        double movieRating;
        int lengthHours;
        int lengthMinutes;

        Scanner inFile;
        try {
            inFile = new Scanner(new File(fileName));

            int numReleases = inFile.nextInt();

            inFile.nextLine();// needed to flush EOL

            for (int i = 0; i < numReleases; i++) {
                movieTitle = inFile.nextLine();
                bondName = inFile.nextLine();
                yearReleased = inFile.nextInt();
                movieRating = inFile.nextDouble();
                lengthHours = inFile.nextInt();
                lengthMinutes = inFile.nextInt();

                inFile.nextLine(); // needed to flush EOL
                movieList.add(new Movie(movieTitle, bondName, yearReleased,
                        movieRating, lengthHours, lengthMinutes));
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void displayInfo() {
        System.out.printf("%-35s", "Film Title");
        System.out.printf("%-15s", "Bond Actor");
        System.out.printf("%7s", "Year");
        System.out.printf("%8s", "Rating");
        System.out.printf("%10s", "Minutes");
        System.out.println();
        System.out.println();
        Iterator<Movie> itr = movieList.iterator();
        Movie temp;
        while (itr.hasNext()) {
            temp = itr.next();
            System.out.printf("%-35s", temp.getTitle());
            System.out.printf("%-15s", temp.getBondActor());
            System.out.printf("%7d", temp.getYearFilmReleased());
            System.out.printf("%8.1f", temp.getFilmRating());
            System.out.printf("%10s", temp.getFilmHrs() * 60 + temp.getFilmMin());
            System.out.println();
            System.out.println();
        }
        displayAveLength();
        displayAveRating();
        Search();
    }

    public void sort() {
        bubbleSort(movieList);
    }

    public void bubbleSort(ArrayList<Movie> list) {
        for (int outer = 0; outer < list.size() - 1; outer++) {
            for (int inner = 0; inner < list.size() - outer - 1; inner++) {
                if (list.get(inner).compareTo(list.get(inner + 1)) > 0) {
                    Movie temp = list.get(inner);
                    list.set(inner, list.get(inner + 1));
                    list.set(inner + 1, temp);
                }
            }
        }
    }

    public void displayAveRating() {
        double average = 0;
        int count = 0;
        for (Movie m : movieList) {
            average += m.getFilmRating();
            count++;
        }
        average /= count;
        System.out.printf("The average rating for a James Bond Movie is %.2f out of a possible 4.0\n", average);
    }

    public void Search() {
        String actor = "Sean Connery";
        double ratingToExceed = 2.0;
        int minutesToExceed = 120;
        int index = sequentialSearch(movieList, actor, ratingToExceed, minutesToExceed);
        if (index != -1) {
            System.out.printf(
                    "Movie with %s as the main actor, a rating of at least %.1f, and a minium time of %d minutes is at index %d\n",
                    actor, ratingToExceed, minutesToExceed, index);
        } else {
            System.out.println("No match found");
        }
    }

    public int sequentialSearch(ArrayList<Movie> list, String dude,
            double rating, int minutes) {
        for (int i = 0; i < list.size(); i++) {
            Movie m = list.get(i);
            if (m.getBondActor().equals(dude) && m.getFilmRating() > rating
                    && m.getFilmHrs() * 60 + m.getFilmMin() > minutes) {
                return i;
            }
        }
        return -1;
    }

    public void displayAveLength() {
        double average = 0;
        int i;
        for (i = 0; i < movieList.size(); i++) {
            average += movieList.get(i).getFilmMin() + movieList.get(i).getFilmHrs() * 60;
        }
        average /= i;
        System.out.printf("The average length for a James Bond Movie is %d hrs and %.1f minutes\n", (int) average / 60,
                average % 60);
    }
}
