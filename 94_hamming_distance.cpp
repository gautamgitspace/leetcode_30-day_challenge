class Solution {
public:
    int hammingDistance(int x, int y) {
        int xorian = x ^ y;
        int count = 0;
        while (xorian) {
            count += xorian & 1;
            xorian >>= 1;
        }
        return count;
    }
};
