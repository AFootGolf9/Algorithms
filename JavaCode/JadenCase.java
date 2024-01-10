public class JadenCase {

	public String toJadenCase(String phrase) {
		if (phrase != null && phrase.length() > 0) {
            String[] words = phrase.split(" ");
            StringBuilder sb = new StringBuilder();
            for (String word : words) {
                sb.append(Character.toUpperCase(word.charAt(0)));
                sb.append(word.substring(1));
                sb.append(" ");
            }
            return sb.toString().trim();
        }
		return null;
	}

}