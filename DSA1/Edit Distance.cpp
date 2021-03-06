class Solution {
public:
    int minDistance(string word1, string word2) {
        int x=word1.length();
        int y=word2.length();
        int dp[x+1][y+1];
        for(int i=0;i<=x;i++){
            for(int j=0;j<=y;j++){
                if(i==0) dp[i][j]=j;
                else if(j==0) dp[i][j]=i;
                else{
                    if(word1[i-1]==word2[j-1]){
                        dp[i][j]=dp[i-1][j-1];
                    }
                    else{
                        dp[i][j]=1+min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]});
                    }
                }
            }
        }
        return dp[x][y];
    }
};
