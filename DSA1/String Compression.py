class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        r = 0
        w = 0
        while r < len(chars):
            char = chars[r]
            count = 0
            while r < len(chars) and chars[r] == char:
                r += 1
                count += 1
            chars[w] = char
            w += 1
            if count > 1:
                for d in str(count):
                    chars[w] = d
                    w += 1
        return w
        
