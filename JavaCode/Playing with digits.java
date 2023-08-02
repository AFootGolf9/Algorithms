public class DigPow {
	
	public static long digPow(int n, int p) {
		long power = -1, sum = 0;
		String num = Integer.toString(n);
		for(int i = 0; i < num.length(); i++) {
			sum += (long) Math.pow((num.charAt(i) - '0'), p + i);
		}
		if (sum % n == 0) power = sum/n;
    return power;
	}
}
