import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

class FrequencySort {
    public static int[] frequencySort(int[] nums) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) {
            numsList.add(num);
        }

        Collections.sort(numsList, (a, b) -> {
            int freqA = frequencyMap.get(a);
            int freqB = frequencyMap.get(b);

            if (freqA != freqB) {
                return freqA - freqB; // Ordena por frequência crescente
            } else {
                return b - a; // Ordena por valor decrescente em caso de empate
            }
        });

        for (int i = 0; i < nums.length; i++) {
            nums[i] = numsList.get(i);
        }

        return nums;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,2,2,2,3};
        int[] result = frequencySort(nums);

        System.out.println(Arrays.toString(result));
    }

}
