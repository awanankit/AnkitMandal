import java.util.Scanner;
public class SimpalCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter second number: ");
        int num2 = scanner.nextInt();
        System.out.println("Sum of " + num1 + " and " + num2 + " is: " + (num1 + num2));
        System.out.println("Difference of " + num1 + " and " + num2 + " is: " + (num1 - num2));
        System.out.println("Product of " + num1 + " and " + num2 + " is: " + (num1 * num2));
        if (num2 != 0) {
            double division = (double) num1 / num2;
            System.out.println("Division of " + num1 + " and " + num2 + " is: " + division);
        } else {
            System.out.println("Error: Division by zero is not allowed.");
        }
    }
}
