#include<iostream>
#include<vector>
#include<stack>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };


class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int deep = 0;
        return is_balanced(root, &deep);
    }
    bool is_balanced(TreeNode* root, int *deep){
        if(root == NULL)
            return true;
        int deep_right = 0;
        int deep_left = 0;
        bool right_balance = is_balanced(root->right, &deep_right);
        bool left_balance = is_balanced(root->left, &deep_left);
        if(right_balance && left_balance && abs(deep_right - deep_left) <= 1){
            *deep = 1 + (deep_left > deep_right? deep_left : deep_right);
            return true;
        }
        else{
            return false;
        }
    }
};

int main(){
    Solution s;
    TreeNode a(1);
    TreeNode b(2);
    TreeNode c(3);
    a.right = &b;
    b.left = &c;
    vector<int> result = s.inorderTraversal(&a);
    for(vector<int>::iterator it = result.begin(); it != result.end(); it++)
        cout << *it << endl;
    return 0;
}
