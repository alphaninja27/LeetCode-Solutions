class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int rows = mat.size(), columns = mat[0].size(), length = rows * columns; 
           
        
        if(length != (r * c)) return mat; 
           
        
        vector<vector<int>> output(r, vector<int>(c));
          
        
        for(int i = 0; i < length; i++) {
            
            output[i / c][i % c] = mat[i / columns][i % columns];
              
                
        
        }
        return output;
    }
};
