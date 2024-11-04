import java.util.Scanner;

public class SankarAndMaths {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        
        
        long distinctElements = (N + 1) / 2;
        
        System.out.println(distinctElements);
        sc.close();
    }
}