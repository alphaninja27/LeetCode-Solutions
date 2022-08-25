class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = [0]
        def merge(l):
            if len(l)<=1:
                return l
            list_A = merge(l[:len(l)//2])
            list_B = merge(l[len(l)//2:])
        
            left = right = 0
        # list_A and list_B are sorted lists, and we can use two-pointer method to count the number of pairs 
            while(left<len(list_A) and right<len(list_B)):
                if list_A[left]<=2*list_B[right]:
                    left+=1
                else:
                    ans[0]+=len(list_A)-left
                    right+=1
        # it is possible to write a faster sort function since list_A and list_B are all sorted lists
            return sorted(list_A+list_B)
        merge(nums)
        return ans[0]
