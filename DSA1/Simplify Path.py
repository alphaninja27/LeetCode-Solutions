class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        dicti = ""
        res = ""
        res += "/"
        l = len(path)
        i = 0
        while i < l:
            dir_str = ""
            while i < l and path[i] == "/":
                i += 1
            while i < l and path[i] != "/":
                dir_str += path[i]
                i += 1
            if dir_str == "..":
                if len(ans):
                    ans.pop()
            elif dir_str == ".":
                continue
            elif len(dir_str) > 0:
                ans.append(dir_str)
            i += 1
        ansr = []
        while len(ans):
            ansr.append(ans[-1])
            ans.pop()
        while len(ansr):
            temp = ansr[-1]
            if len(ansr) != 1:
                res += temp + "/"
            else:
                res += temp
            ansr.pop()
        return res 
