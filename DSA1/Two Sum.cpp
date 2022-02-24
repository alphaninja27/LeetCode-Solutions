class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int x=0;
        int sum=0;
        vector<int>ans={0,0};
        for(int i =0; i<nums.size();i++)
            {
                for (int j =i+1; j<nums.size(); j++)
                {
                    sum=nums.at(i)+nums.at(j);
                    if(sum==target){
                       ans.at(0)=i;
                       ans.at(1)=j;
                       
                    }
                }
            }
      return ans;
    }
};
