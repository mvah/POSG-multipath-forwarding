import java.util.ArrayList;
import java.util.List;

public class GenerationArbre {

    public static List<String> generate(Element element) {
        List<String> result = new ArrayList<>();
        StringBuilder combination = new StringBuilder();
        generateHelper(result, combination, element.getValue(), 0, element.getTaille()-1);
        return result;
    }

    private static void generateHelper(List<String> result, StringBuilder combination, String str, int start, int p) {
        if (combination.length() == p) {
            result.add(combination.toString());
            return;
        }
        for (int i = start; i < str.length(); i++) {
            combination.append(str.charAt(i));
            generateHelper(result, combination, str, i + 1, p);
            combination.deleteCharAt(combination.length() - 1);
        }
    }
}
