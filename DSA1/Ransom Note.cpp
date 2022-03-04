class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        for(int i=0; i<ransomNote.size(); i++)
        {
            bool temp = false;
            for(int j=0; j<magazine.size(); j++)
            {
                if(ransomNote[i] == magazine[j])
                {
                    magazine[j] = '0';
                    temp = true;
                    break;
                }
            }
            if(temp == false)
                return false;
        }
        return true;
    }
};
