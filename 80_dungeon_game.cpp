class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        
        /* get basic business done */
        int m = dungeon.size();
        int n = dungeon[0].size();
        int hp[m + 1][n + 1];
        
        /* INIT 
         * - we add dummy row and col to define boundaries and set it to inf
         *   so that we don't consider that move as we need to save the P in 
         *   minimum moves possible.
         *
         * - we set hp[m - 1][n] and hp[n - 1][m] to 1 based on the assumption
         *   that we can save the P even with 1 hp (bare minimum to be alive) */
        for(int i = 0; i < m + 1; i++) hp[i][n] = INT_MAX;
        for(int i = 0; i < n + 1; i++) hp[m][i] = INT_MAX;
        
        hp[m][n-1] = 1;
        hp[m-1][n] = 1;
        
        /* actual business:
         *
         * if we define : dp[i][j] = minimum cost from (0, 0) to (i, j)
         * It won't help solving the problem, because the result of 
         * dp[i + 1][j + 1] does not depend only on previous solve 
         * subproblems, but also future unsolved subproblems. So, how 
         * about let's define the subproblem from the other end of the 
         * puzzle?
         *
         * dp[i][j] = minimum health level required to reach the princess
         * when entering (i, j)
         * 
         * So, what is dp[i + 1][j + 1] then? It depends on the minimum 
         * between dp[i][j + 1] and dp[i + 1][j], because we want to choose
         * the cheapest way to go. Of course we also need to add or deduct
         * the value from dungeon matrix 
         * 
         * The way to look at it is we want to reach either grid[i + 1][j]
         * or grid[i][j + 1] with health = 1
         * So if we want to reach grid[1][1] alive and neither gain/lose 
         * health in dungeon[1][1] (i.e. if dungeon[1][1] = 0), we need
         * at least the health required to reach grid[1][2] or grid[2,1] 
         * i.e. min( hp[1][2], hp[2][1] ). This is nothing but deciding
         * the minimum between the two choice of moves and making the orb
         * (-ve or +ve) react with that move (add to the move)
         * 
         * moving forward with this decision, we find max of above and 1. As
         * explained earlier, bare minimum hp can be 1 and sometimes it will
         * become negative during the course and we need to be alive so in 
         * those cases we max of the two which is 1 */
        
        for(int i = m - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                hp[i][j] = max (min (hp[i+1][j], hp[i][j+1]) - dungeon[i][j], 1);
            }
        }
    return hp[0][0];
    }
};
