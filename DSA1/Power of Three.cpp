class Solution {
public:
    bool isPowerOfThree(int n) {
        long x=1;
        for(int i=0;i<31;i++){
            if(x==n){
                return true;
            }
            x=x*3;
        }
        return false;
    }
};
