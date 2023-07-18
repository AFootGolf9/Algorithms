class Solution {
		public static String rangeExtraction(int[] arr) {
		String output = "";
		int[] hold = new int[] {arr[0], 0};
		int holded = 1;
		
		for(int i = 1; i <  arr.length; i++) {	
			
			switch(holded) {
			case 0:
				if(arr[i] != arr[i-1] + 1) {
					output = output + String.valueOf(arr[i]) + ","; 
				}
				break;
			case 1:
				if(arr[i] != arr[i-1] + 1) {
					output = output + String.valueOf(hold[0]) + ",";
					hold = new int[2];
					holded = 0;
				}
				break;
			case 2:
				if(arr[i] != arr[i-1] + 1) {
					output = output + String.valueOf(hold[0]) + "," + String.valueOf(hold[1]) + ",";
					hold = new int[2];
					holded = 0;
				}
				break;
			case 3:
				if(arr[i] != arr[i-1] + 1) {
					output = output + String.valueOf(hold[0]) + "-" + String.valueOf(hold[1]) + ",";
					hold = new int[2];
					holded = 0;
				}
			}
			switch(holded) {
			case 0:
				hold[0] = arr[i];
				holded ++;
				break;
			case 1:
				hold[1] = arr[i];
				holded++;
				break;
			case 2:
				
				hold[1] = arr[i];
				holded ++;
				break;
			case 3:
				hold[1] = arr[i];
			}
			
		}
		
		switch(holded) {
		case 1:
			output = output + String.valueOf(hold[0]);
			break;
		case 2:
			output = output + String.valueOf(hold[0]) + "," + String.valueOf(hold[1]);
			break;
		case 3 :
			output = output + String.valueOf(hold[0]) + "-" + String.valueOf(hold[1]);
		}
		
		
		return output;
}
}
