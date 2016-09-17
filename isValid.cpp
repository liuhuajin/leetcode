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
    bool isValid(string s) {
        stack<char> st;
        for(int i = 0; i < s.length(); i++){
            if(st.empty()){
                st.push(s[i]);
            }
            else{
                if((s[i] == ']' && st.top() == '[') || (s[i] == ')' && st.top() == '(') || (s[i] == '}' && st.top() == '{') )
                {
                    st.pop();
                }
                else{
                    st.push(s[i]);
                }
            }
        }
        return st.empty();
    }
};



int main(){
    Solution s;
    return 0;
}
