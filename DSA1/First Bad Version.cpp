class Solution {
public:
    int firstBadVersion(int n) {
        long s=1,e=n;
        while(true){
            int mid=(s+e)/2;
            if(isBadVersion(mid)){
                if((mid-1>0&&!isBadVersion(mid-1))||mid==1){
                    return mid;
                }else{
                    e=mid-1;
                }
            }else{
                s=mid+1;
            }
            if(s>e){
                return -1;
            }
            
        }
    }
};
