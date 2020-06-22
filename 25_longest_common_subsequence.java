class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // base condition
        if(text1.length()==0||text2.length()==0) return 0;
        // init dp
        int dp[][] = new int[text1.length()+1][text2.length()+1];

        // outer, inner loops and i,j translation
        for(int i=1;i<text1.length()+1;i++){
            for(int j=1;j<text2.length()+1;j++){
                // match, add lcs +1
                if(text1.charAt(i-1)==text2.charAt(j-1)) { dp[i][j]=dp[i-1][j-1]+1; }
                // no match
                else { dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]); }
            }
        }
        return dp[text1.length()][text2.length()];
    }
}
