class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int pos = m+n-1;
        m -= 1;
        n -= 1;
        while (n >= 0) {
            nums1[pos--] = (m >= 0 && nums1[m] > nums2[n]) ? nums1[m--] : nums2[n--];
        }
    }
};
