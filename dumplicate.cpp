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
    int removeDuplicates(vector<int>& nums) {
        int first = 0;
        int last = 0;
        if(nums.size() == 0)
            return 0;
        while(last < nums.size()){
            if(nums[first] == nums[last]){
                ++last;
            }
            else{
                nums[first+1] = nums[last];
                ++last;
                ++first;
            }
        }
        return first+1;
    }
};


int main(){
    Solution s;
    return 0;
}
