class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) <= k:
            return 0
        dicti = {}
        for n in arr:
            if n not in dicti:
                dicti[n] = 0
            dicti[n] += 1
        minheap = []
        for numer, amount in dicti.items():
            heappush(minheap, (amount, n))
        while k > 0 and len(minheap) > 0:
            amount, n = heappop(minheap)
            k -= amount
        l = len(minheap)
        return l if k >= 0 else l + 1
