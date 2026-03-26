import java.util.Scanner;
public class Area { 
   @SuppressWarnings("ConvertToTryWithResources")
   public static void main (String[] args){
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter Length:");
    int Length= scanner.nextInt();
    System.out.println("Enter Breth:");
    int Breth= scanner.nextInt();
    int area = Length*Breth;
    System.out.println("The area is:" +area);
    scanner.close();
   } 
}