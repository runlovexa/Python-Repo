import java.util.Scanner;

public class LastEvenNumber {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int lastEvenNumber = -1; // Initialize to -1 to handle cases where all elements are odd

        for (int i = 0; i < N; i++) {
            int num = scanner.nextInt();
            if (num % 2 == 0) { // Check if the current number is even
                lastEvenNumber = num;
            }
        }

        System.out.println(lastEvenNumber);
    }
}