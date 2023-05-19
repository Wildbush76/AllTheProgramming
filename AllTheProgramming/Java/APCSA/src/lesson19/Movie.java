package lesson19;

public class Movie implements Comparable {
    private String myTitle; // title of Bond film
    private String myBondActor; // name of actor who portrayed James Bond
    private int myYear; // year film was released
    private double myFilmRating;// from all-reviews.com
    private int myLengthHours; // hours (truncated) portion of film length
    private int myLengthMinutes;// minutes beyond truncated hours

    public Movie(String title, String name, int yr, double rating, int hrs, int min) {
        myTitle = title;
        myBondActor = name;
        myYear = yr;
        myFilmRating = rating;
        myLengthHours = hrs;
        myLengthMinutes = min;
    }

    public String getTitle() {
        return myTitle;
    }

    public String getBondActor() {
        return myBondActor;
    }

    public int getYearFilmReleased() {
        return myYear;
    }

    public double getFilmRating() {
        return myFilmRating;
    }

    public int getFilmHrs() {
        return myLengthHours;
    }

    public int getFilmMin() {
        return myLengthMinutes;
    }

    public int compareTo(Object other) {
        System.out.println("what trying to compare");
        return 0;
    }

    public int compareTo(Movie other) {
        return myYear - other.getYearFilmReleased();
    }

    public String toString() {
        return (myTitle + " " + myBondActor + " " + myYear + " " + myFilmRating
                + " " + myLengthHours + " hr " + myLengthMinutes + " min");
    }
}
