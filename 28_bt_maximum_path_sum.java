public class Solution {
    int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        helper(root);
        return max;
    }

    int helper(TreeNode root) {
        /* base condition */
        if (root == null) return 0;

        /* compute left_gain and right_gain recursively
         * to enterain negative node values, take 0 as
         * a dummy. that way we take max of 0 and +ve
         * values */
        int left_gain = Math.max(helper(root.left), 0);
        int right_gain = Math.max(helper(root.right), 0);

        /* this max variable compares the max value from each
         * iteration with the current sum (i.e. root, left and
         * right). then we update it */
        max = Math.max(max, root.val + left_gain + right_gain);

        /* At each node, we need to make a decision if the
         * sum comes from the left path or the right path,
         * if left, we pick the left path plus the current
         * node's value */
        return root.val + Math.max(left_gain, right_gain);
    }
}
