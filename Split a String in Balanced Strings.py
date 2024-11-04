import java.util.Scanner;

public class BalancedStringSplitter {
    public static int balancedStringSplit(String s) {
        int balanceCount = 0; // To keep track of balance between 'L' and 'R'
        int splitCount = 0;   // To count the number of balanced substrings

        for (char c : s.toCharArray()) {
            // Increment or decrement the balance based on the character
            if (c == 'L') {
                balanceCount++;
            } else if (c == 'R') {
                balanceCount--;
            }

            // Whenever the balance is zero, we found a balanced substring
            if (balanceCount == 0) {
                splitCount++;
            }
        }

        return splitCount;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine().trim();
        int result = balancedStringSplit(inputString);
        System.out.println(result);
        scanner.close();
    }
}