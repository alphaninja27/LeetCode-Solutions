class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> n;
        for(int i=0;i<nums.size();i++){
            n.push_back(nums[i]*nums[i]);
        }
        sort(n.begin(),n.end());
        return n;
    }
};
