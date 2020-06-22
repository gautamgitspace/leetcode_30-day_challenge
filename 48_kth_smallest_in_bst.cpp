class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        /* Push everything in left branch to the stack
         * with an assumption that smallest will be in
         * in the left sub (BST)
         */
        while (root != NULL) {
            s.push(root);
            root = root->left;
        }
        /* now keep popping from stack and at each pop also
         * check if the popped element has a right sub. If it
         * has, we need to investigate the 'left' portion of
         * this branch. So we push that to the stack as well */
        while (k--) {
            TreeNode* curr = s.top();
            s.pop();
            if (k == 0) return curr->val;
            TreeNode* right = curr->right;
            while (right != NULL) {
                s.push(right);
                right = right->left;
            }
        }
        return -1;
    }
};
