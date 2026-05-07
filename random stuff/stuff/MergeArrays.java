import java.util.Scanner;
import java.util.Arrays;
//import java.util.Math;

public class MergeArrays {
    public static void main(String[] args) {
        int num = 987654321;
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            sum *= 10;
            num /= 10;
        }
        sum = sum / 10;
        System.out.println(sum);
        // Scanner in = new Scanner(System.in);
        // long i = 0;
        // while (i != -1) {
        // long a = i + 0L;
        // long b = i + 1L;
        // long c = i + 2L;
        // long d = i + 3L;
        // boolean ans = ((a * a * a * a) + (b * b * b * b) + (c * c * c * c)) == (d * d
        // * d * d);
        // System.out.println(ans);
        // System.out.println(i);
        // i++;
        // in.close();
        // }

        /*
         * int arr[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90 };
         * for (int j = 0; j < 21 % 9; j++) {
         * 
         * int temp = arr[0];
         * for (int i = 0; i < arr.length - 1; i++) {
         * arr[i] = arr[i + 1];
         * }
         * arr[arr.length - 1] = temp;
         * 
         * System.out.println(Arrays.toString(arr));
         * }
         */
        /*
         * int a = 2;
         * for (int i = 1; i <= 500000000; i++) {
         * int cal = i * a;
         * System.out.print(i);
         * System.out.print(" x  = ");
         * System.out.println(cal);
         * }
         */
        /*
         * Scanner in = new Scanner(System.in);
         * int num = (int) (Math.random() * 100);
         * int guess = 0;
         * while (num != guess) {
         * guess = in.nextInt();
         * if (guess < num) {
         * System.out.println("less");
         * }
         * if (guess > num) {
         * System.out.println("more");
         * }
         * 
         * }
         */
        /*
         * int[] arr1 = { 1, 2, 3 };
         * int[] arr2 = { 4, 5, 6 };
         * 
         * int[] mergedArray = mergeArrays(arr1, arr2);
         * 
         * System.out.println("Merged Array: " + Arrays.toString(mergedArray));
         * }
         * 
         * public static int[] mergeArrays(int[] arr1, int[] arr2) {
         * int length1 = arr1.length;
         * int length2 = arr2.length;
         * int[] mergedArray = new int[length1 + length2];
         * 
         * for (int i = 0; i < length1; i++) {
         * mergedArray[i] = arr1[i];
         * }
         * 
         * for (int i = 0; i < length2; i++) {
         * mergedArray[length1 + i] = arr2[i];
         * }
         * 
         * return mergedArray;
         */
    }
}