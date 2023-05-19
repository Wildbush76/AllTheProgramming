package lesson11;

public class Teacher extends Person {
    private double salary;
    private String subject;

    public Teacher(String name, int age, String gender, String teachings, double earning) {
        super(name, age, gender);
        salary = earning;
        subject = teachings;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String newSubject) {
        subject = newSubject;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double newSalary) {
        salary = newSalary;
    }

    public String toString() {
        return super.toString() + ", subject: " + subject + ", salary: " + salary;
    }
}