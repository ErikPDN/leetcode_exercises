
public class CountNumbersOfTeams {
    public static int numTeams(int[] rating) {
        if (rating.length < 3) {
            return 0;
        }

        int count = 0;
        int n = rating.length;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if ((rating[i] < rating[j] && rating[j] < rating[k])
                            || (rating[i] > rating[j] && rating[j] > rating[k])) {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] rating = { 1,2,3,4};

        System.out.println(numTeams(rating));
    }

}
