import java.util.Scanner;

public class MonkAndWelcome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        int N = sc.nextInt();

        
        int[] A = new int[N];
        int[] B = new int[N];

        
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        
        for (int i = 0; i < N; i++) {
            B[i] = sc.nextInt();
        }

       
        int[] C = new int[N];

       
        for (int i = 0; i < N; i++) {
            C[i] = A[i] + B[i];
        }

     
        for (int i = 0; i < N; i++) {
            System.out.print(C[i] + " ");
        }
    }
}
