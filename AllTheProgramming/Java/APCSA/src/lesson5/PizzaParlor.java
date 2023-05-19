package lesson5;

class PizzaParlor {
    // instance variables
    private int myNumCheesePizzas; // # of cheese pizzas
    private int myNumPeppPizzas; // # of pepperoni pizzas
    private int myNumVegPizzas; // # of veggie pizzas
    private int myCheeseSupply; // ounces of cheese
    private int myPepperoniSupply;// ounces of pepperoni
    private int myVeggieSupply; // ounces of veggies
    private double myRevenue; // dollars collected
    private double myOrigAcctBal;// original bank account balance
    private int doughSupply;

    // constructor
    PizzaParlor() {
        myNumCheesePizzas = 0;
        myNumPeppPizzas = 0;
        myNumVegPizzas = 0;
        myCheeseSupply = 400;
        myPepperoniSupply = 200;
        myVeggieSupply = 200;
        myRevenue = 0;
        myOrigAcctBal = 1000;
        doughSupply = 400;
    }

    // methods
    int getDoughSupply() {
        return doughSupply;
    }

    void orderCheese() {
        myNumCheesePizzas++;
        myRevenue += 8;// cheese pizza price:$8
        myCheeseSupply -= 12;// cheese needed per cheese pizza
        doughSupply -= 11;
    }

    void orderPepperoni() {
        myNumPeppPizzas++;
        myRevenue += 10;// pepperoni pizza price:$10
        myCheeseSupply -= 8;// cheese needed per pepp pizza
        myPepperoniSupply -= 6;// pepperoni needed per pepp pizza
        doughSupply -= 11;
    }

    void orderVeggie() {
        myNumVegPizzas++;
        myRevenue += 11;// veggie pizza price:$11
        myCheeseSupply -= 8;// cheese needed per veggie pizza
        myVeggieSupply -= 12;// veggies needed per veggie pizza
        doughSupply -= 11;
    }

    int getNumCheesePizzas() {
        return myNumCheesePizzas;
    }

    int getNumPepperoniPizzas() {
        return myNumPeppPizzas;
    }

    int getNumVeggiePizzas() {
        return myNumVegPizzas;
    }

    int getCheeseSupply() {
        return myCheeseSupply;
    }

    int getPepperoniSupply() {
        return myPepperoniSupply;
    }

    int getVeggieSupply() {
        return myVeggieSupply;
    }

    double getRevenueTotal() {
        return myRevenue;
    }

    double getBankAccountBalance() {
        return myOrigAcctBal + myRevenue;
    }
}
