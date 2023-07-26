class Solution {
    public static String whoLikesIt(String... names) {
        String output = "";
        switch (names.length) {
            case 0:
              output = "no one likes this";
              break;
            case 1:
              output = names[0] + " likes this";
              break;
            case 2:
              output = names[0] + " and " + names[1] + " like this";
              break;
            case 3:
              output = names[0] + ", " + names[1] + " and " + names[2] + " like this";
              break;
            default:
              output = names[0] + ", " + names[1] + " and " + (names.length - 2) + " others like this";
        }
        return output;
    }
}
