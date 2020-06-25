/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        
        int left_height = 0, right_height = 0;
        
        TreeNode *l = root, *r = root;
        
        /* find left and right heights 8*/
        while (l) {
            left_height ++;
            l = l->left;
        }
        
        while (r) {
            right_height ++;
            r = r->right;
        }
        /* fits criterion for a full binary tree AKA perfect BT */
        if (left_height == right_height) return pow(2, left_height) - 1;
        
        /* else find left height, find right height and 1 for root */
        return 1 + countNodes(root->left) + countNodes(root->right);
        
    }
};
