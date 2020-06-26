class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return sumNodes(root, 0);
    }
    int sumNodes(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        int running_sum = sum * 10 + root->val;
        
        // nothing more to traverse, return the calculated sum
        if (root->left == NULL && root->right == NULL) return running_sum;

        int left_sum = sumNodes(root->left, running_sum);
        int right_sum = sumNodes(root->right, running_sum);
        
        return left_sum + right_sum;
    }
};
