import java.util.Scanner;
public class Multiplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter second number: ");
        int num2 = scanner.nextInt();
        int product = num1 * num2;
        System.out.println("Product of " + num1 + " and " + num2 + " is: " + product);
    }
}
