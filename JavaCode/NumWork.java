public class NumWork {
    public static int[] countPositivesSumNegatives(int[] input){
        if(input == null || input.length == 0) return new int[0];
        int[] out = new int[]{0,0};
        for(int i = 0; i < input.length; i++){
            if(input[i] > 0){
                out[0]++;
            }else out[1] += input[i];
        }
        return out;
    }
}