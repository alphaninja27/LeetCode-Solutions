class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j=0;
       int i=0;
       for(;i<nums.size();i++){
           if(nums[i]!=0){
               nums[j]= nums[i];
               j++;
           }
       }
        
        int dif = i-j;
        while(dif>0){
            nums[j]= 0;
            j++;
            dif--;
        }
    }
};
