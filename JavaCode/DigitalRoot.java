public class DRoot {
  public static int digital_root(int output) {
    String hold = String.valueOf(output);
        while(output > 9){
            hold = String.valueOf(output);
            output = 0;
            
            for (int i = 0; i < hold.length(); i ++){
                output = output + Integer.parseInt(hold.substring(i, i + 1));
            }  
        }
    return output;
  }
}
