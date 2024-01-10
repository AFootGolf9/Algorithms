import java.util.Arrays;

public class DescendingOrder {
  public static int sortDesc(final int num) {
    String numString = Integer.toString(num);
    char[] numArray = numString.toCharArray();
    Arrays.sort(numArray);
    String sortedNumString = new StringBuilder(new String(numArray)).reverse().toString();
    return Integer.parseInt(sortedNumString);
  }
}