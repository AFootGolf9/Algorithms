import java.util.Scanner;

public class LCS {
    public static String lcs(String x, String y) {
        String out  = "";
        String bigStr = null;
        String smlStr = null;
        if (x.length() < y.length()) {
            bigStr = y;
            smlStr = x;
        }else{
            bigStr = y;
            smlStr = x;
        }
        char[] holdEqual = new char[bigStr.length()];
        for(int i = 0; i < smlStr.length(); i++){
            for(int j = 0; j < bigStr.length(); j++){
                if (smlStr.charAt(i) == bigStr.charAt(j)){
                    holdEqual[j] = bigStr.charAt(j);
                }
            }
        }
        for(int i = 0; i < holdEqual.length; i++){
            if(holdEqual[i] != ' '){
                out += holdEqual[i];
            }
        }
        return out;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println(lcs(scan.nextLine(), scan.nextLine()));;
    }
}
