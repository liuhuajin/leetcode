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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        TreeNode *pre = NULL;
        TreeNode *cur = NULL;
        vector<int> result;
        if(root != NULL)
            st.push(root);
        while(!st.empty()){
            cur = st.top();
            if((cur->left == NULL && cur->right == NULL) ||
               (pre != NULL && (cur->left == pre || cur->right == pre))){
                result.push_back(cur->val);
                st.pop();
                pre = cur;
            }
            else{
                if(cur->right)
                    st.push(cur->right);
                if(cur->left)
                    st.push(cur->left);
            }
        }
        return result;
    }
};


int main(){
    Solution s;
    TreeNode a(1);
    TreeNode b(2);
    TreeNode c(3);
    a.right = &b;
    b.left = &c;
    vector<int> result = s.postorderTraversal(&a);
    for(vector<int>::iterator it = result.begin(); it != result.end(); it++)
        cout << *it << endl;
    return 0;
}