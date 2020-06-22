class Solution {
    public int change(int amount, int[] coins) {
        int [][]dp = new int[coins.length + 1][amount + 1];

        /* INIT */
        for (int i = 0; i < coins.length + 1; i++) {
            for (int j = 0; j < amount + 1; j++) {
                if (i == 0) dp[i][j] = 0;
                if (j == 0) dp[i][j] = 1;
            }
        }

        /* CHOICE DIAGRAM */
        for (int i = 1; i <= coins.length; i++) {
            for (int j = 1; j <= amount; j++) {
                dp[i][j] = dp[i - 1][j];
                if (coins[i - 1] <= j) {
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j];
                }

            }
        }
        return dp[coins.length][amount];
    }
}

/* optimized solution, but 2d */

class Solution {
    public int change(int amount, int[] coins) {
        int [][]dp = new int[coins.length + 1][amount + 1];
        dp[0][0] = 1;

        for (int i = 1; i <= coins.length; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= amount; j++) {
                /* we cannot pick item, just process it */
                dp[i][j] = dp[i - 1][j];
                if (coins[i - 1] <= j) {
                    /* we can pick item, process it (multiple times) or not*/
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j];
                }
            }
        }
        return dp[coins.length][amount];
    }
}
