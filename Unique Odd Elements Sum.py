import java.util.HashSet;
import java.util.Scanner;

public class UniqueOddElementsSum {

    public static int sumUniqueOdd(int[] arr) {
        HashSet<Integer> uniqueOdd = new HashSet<>();
        int sum = 0;
        for (int num : arr) {
            if (num % 2 != 0 && uniqueOdd.add(num)) {
                sum += num;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

        int uniqueOddSum = sumUniqueOdd(arr);
        System.out.println(uniqueOddSum);
    }
}