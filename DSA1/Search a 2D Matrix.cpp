class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int s=0;
        int r=matrix.size();
        int c=matrix[0].size();
        int e=r*c-1;
        int mid=s+(e-s)/2;// means the same as (s+e)/2

    while(s<=e){ //s<=e means when the search space gets reduced to 1                           element we will check whether that is target                                element or not
        int ele=matrix[mid/c][mid%c];
        if(ele==target)
            return 1;
        else if (target>ele)// note 1:(see below)
            s=mid+1;
        else
            e=mid-1;
    
        mid=(s+e)/2;
    }
    return 0;
    }
    
};
