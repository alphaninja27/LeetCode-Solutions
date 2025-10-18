class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
         l = 0
         h = len(arr) - k
         while l < h:
            m = l + (h - l) // 2
            if x <= arr[m]:
                h = m
            elif arr[m + k] <= x:
                l = m + 1
            else:
                mid = abs(x - arr[m])
                midk = abs(x - arr[m + k])
                if mid <= midk:
                    h = m
                else:
                    l = m + 1
         return arr[l:l + k]
