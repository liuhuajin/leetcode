#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> num_to_index;
        vector<int> result;
        for(vector<int>::iterator it=nums.begin(); it != nums.end(); it++){
        	if(num_to_index.count(target - *it) == 1){
        		result.push_back(it - nums.begin());
        		result.push_back(num_to_index[target-*it]);
        	}
        	else{
        		num_to_index.insert(make_pair(*it, it-nums.begin()));
        	}
        }
        return result;
    }
};

int main()
{
	Solution s;
	vector<int> nums;
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(4);
	vector<int> result = s.twoSum(nums, 6);
    for(vector<int>::iterator it = result.begin(); it != result.end(); it++){
        cout << *it << endl;
    } 
}
