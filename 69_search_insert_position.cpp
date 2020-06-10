class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        while (low <= high) {
            int mid = low + (high - low)/2;
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        /* returning low ensures that index is
         * returned if item exists, otherwise
         * position is returned where it should
         * have existed */
        return low;
    }
};
