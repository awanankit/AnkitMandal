import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter any number:");
        int num = scanner.nextInt();
        int sum=(num+num);
        int sub=(num-num);
        int mul=(num*num);
        int div=(num/num);
        System.out.println("Sum: " + sum);
        System.out.println("Subtraction: " + sub);
        System.out.println("Multiplication: " + mul);
        System.out.println("Division: " + div);
    }
}
