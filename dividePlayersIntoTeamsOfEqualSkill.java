import java.util.Arrays;

class Solution {
    public static void main(String[] args) {
        int[] skill = { 3, 2, 5, 1, 3, 4 };
        System.out.println();
        System.out.println("Result: " + dividePlayers(skill));
    }

    public static long dividePlayers(int[] skill) {
        Arrays.sort(skill);

        int beginPointer = 0;
        int endPointer = skill.length - 1;
        int checkerSum = skill[0] + skill[endPointer];
        long totalSum = 0;

        while (beginPointer < endPointer) {
            if (skill[beginPointer] + skill[endPointer] == checkerSum) {
                totalSum += skill[beginPointer] * skill[endPointer];
                beginPointer++;
                endPointer--;
            } else
                return -1;
        }

        return totalSum;
    }
}