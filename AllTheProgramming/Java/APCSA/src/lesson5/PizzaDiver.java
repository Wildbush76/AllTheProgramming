package lesson5;

public class PizzaDiver {

    public static void main(String[] args) {

        PizzaParlor diner = new PizzaParlor();
        diner.orderCheese();
        diner.orderCheese();
        diner.orderCheese();
        diner.orderPepperoni();
        diner.orderPepperoni();
        diner.orderPepperoni();
        diner.orderPepperoni();
        diner.orderVeggie();
        diner.orderVeggie();
        diner.orderVeggie();
        System.out.println("# of Cheese ordered is " + diner.getNumCheesePizzas());
        System.out.println("# of Pepperoni ordered is " + diner.getNumPepperoniPizzas());
        System.out.println("# of Veggie ordered is " + diner.getNumVeggiePizzas());
        System.out.print("\nRemaining supply of cheese in ounces is: ");
        System.out.println(diner.getCheeseSupply());
        System.out.print("Remaining supply of pepperoni in ounces is: ");
        System.out.println(diner.getPepperoniSupply());
        System.out.print("Remaining supply of veggies in ounces is: ");
        System.out.println(diner.getVeggieSupply());
        System.out.print("Remaining supply of dough in ounces is: ");
        System.out.println(diner.getDoughSupply());
        System.out.println("\nRevenue is $" + diner.getRevenueTotal());
        System.out.println("Bank balance is now $" + diner.getBankAccountBalance());
    }
}