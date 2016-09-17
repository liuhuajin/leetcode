#include<iostream>
#include<vector>
#include<stack>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    vector<string> generateParenthesis(int n) {
       _n = n; 
       string temp = "";
       search(0, 0, temp);
       return result;
    }
    void search(int left, int right, string temp){
        if(right == left && right == _n)
        {
            result.push_back(temp);
            return;
        }
        if(left > right)
            return;
        if(left == _n){
            search(left, right+1, temp+')');
        }
        else{
            search(left+1, right, temp+'(');
            search(left, right+1, temp+')');
        }
    }
private:
    vector<string> result;
    int _n;
};


int main(){
    Solution s;
    return 0;
}
