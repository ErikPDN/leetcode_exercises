import java.util.HashMap;
import java.util.Arrays;
import java.util.Collections;

class Main {
    public static void main(String[] args) {
        String[] names = { "Mary", "John", "Emma" };
        int[] heights = { 180, 165, 170 };

        // Usar a classe Helper para chamar o método sortPeople
        String[] results = Helper.sortPeople(names, heights);

        for (String result : results) {
            System.out.println(result);
        }
    }
}

// Renomear a classe Solution para Helper
class Helper {
    public static String[] sortPeople(String[] names, int[] heights) {
        HashMap<Integer, String> heightsMap = new HashMap<>();

        for (int i = 0; i < names.length; i++) {
            heightsMap.put(heights[i], names[i]);
        }

        Integer[] heightsInteger = Arrays.stream(heights).boxed().toArray(Integer[]::new);
        Arrays.sort(heightsInteger, Collections.reverseOrder());
        String[] sortNames = new String[heights.length];

        for (int i = 0; i < heightsInteger.length; i++) {
            sortNames[i] = heightsMap.get(heightsInteger[i]);
        }

        return sortNames;
    }
}
