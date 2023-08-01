public class NumberUtils {

    public static boolean isNarcissistic(int number) {
        String hold = String.valueOf(number);
        int sum = 0, digit = 0;
        for (int i = 0; i < hold.length(); i++){
            digit = hold.charAt(i) - '0';
            sum = (int) (sum + Math.pow(digit, hold.length())) ;
        }
        return sum == number;
    }

}
