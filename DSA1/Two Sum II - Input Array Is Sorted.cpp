class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
         vector<int>res;
        int s=0;
        int e=numbers.size()-1; 
        while(s<e){
            if(numbers[s]+numbers[e]==target){
                res.push_back(s+1);
                res.push_back(e+1);
                return res;
            }
            if(numbers[s]+numbers[e]>target){
                e--;
            }
            else{
                s++;
            }
        }
        
        return res;
    }
};
