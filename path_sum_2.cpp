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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        target = sum;
        int _sum = 0;
        vector<int> result;
        dfs(root, _sum, result);
        return result_list;
        
    }
    void dfs(TreeNode *root, int _sum, vector<int> result){
        if(root == NULL)
            return;
        if(root->left == NULL && root->right == NULL){
            if(_sum+root->val == target){
                result.push_back(root->val);
                result_list.push_back(result);
            }
            return;
        }
        result.push_back(root->val);
        dfs(root->left, _sum+root->val, result);
        dfs(root->right, _sum+root->val, result);
    }
    
private:
    vector<vector<int>> result_list;
    int target;
};

int main(){
    Solution s;
    return 0;
}