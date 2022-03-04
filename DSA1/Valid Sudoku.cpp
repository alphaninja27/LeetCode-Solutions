class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
       unordered_set<string> set_seen;
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0';
                    //hash code for the element with that row
                    string s_row = "row" + to_string(i) + to_string(num);
                    //hashcode for the element with that column
                    string s_col = "col" + to_string(j) + to_string(num);
                    //haashcode for the element with that 3*3 matrix or box
                    string s_box = "box" + to_string(i/3 * 3 + j/3) + to_string(num);
                    
                //now checking whether these hashcode are already present or not in set
                    if(set_seen.find(s_row) != set_seen.end() || set_seen.find(s_col) != set_seen.end() || set_seen.find(s_box) != set_seen.end() ) return false;
                    
                    
                    else{
                        //now inserting these hascodes in the hash set
                        set_seen.insert(s_row);
                        set_seen.insert(s_col);
                        set_seen.insert(s_box);
                    }
                    
                }
            }
        }
        return true;
    }
};
