import java.util.*;

public class ArrayIteration {
    public static void main(String[] args) {
        int[] numbers = { 10, 20, 30, 40, 50 };

        // 1. Using a traditional for loop
        System.out.println("Using for loop:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // 2. Using a for-each loop
        System.out.println("\nUsing for-each loop:");
        for (int num : numbers) {
            System.out.println(num);
            int a = Math.random();
        }

        // 3. Using a while loop
        System.out.println("\nUsing while loop:");
        int i = 0;
        while (i < numbers.length) {
            System.out.println(numbers[i]);
            i++;
        }

        // 4. Using Java Streams (Java 8+)
        System.out.println(numbers.length);
        java.util.Arrays.stream(numbers).forEach(System.out::println);
    }
}
