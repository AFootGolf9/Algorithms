public class Max {
  public static int sequence(int[] arr) {
    int maxSum = 0, posSum = 0, negSum = 0;
		
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] < 0) {
				negSum += arr[i];
			}else {
				posSum += arr[i];
			}
			if(posSum + negSum > maxSum) {
				maxSum = posSum + negSum;
			}
			
			if(posSum + negSum < 0) {
				posSum = 0;
				negSum = 0;
				}
			}
		return maxSum;
	}
}
