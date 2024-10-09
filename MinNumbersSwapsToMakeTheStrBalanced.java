public class MinNumbersSwapsToMakeTheStrBalanced {
    public static void main(String[] args) {
        String s = "[[][";
        System.out.println(s);
        System.out.println("Result: " + minSwaps(s));

    }

    public static int minSwaps(String s) {
        int imbalance = 0;
        int max_imbalance = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                imbalance++;
            } else {
                imbalance--;
            }

            if (imbalance < 0) {
                max_imbalance = Math.max(max_imbalance, -imbalance);
            }
        }

        return (int) (max_imbalance + 1) / 2;
    }
}
