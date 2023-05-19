package lesson11;

public class CollegeStudent extends Student {
    private String myMajor;
    private int myYear;

    public CollegeStudent(String name, int age, String gender, String idNum, double gpa, int year, String major) {
        super(name, age, gender, idNum, gpa);
        myMajor = major;
        myYear = year;
    }

    public String getMajor() {
        return myMajor;
    }

    public int getYear() {
        return myYear;
    }

    public void setMajor(String newMajor) {
        myMajor = newMajor;
    }

    public void setYear(int newYear) {
        myYear = newYear;
    }

    public String toString() {
        return super.toString() + ", year: " + myYear + ", major: " + myMajor;
    }
}
