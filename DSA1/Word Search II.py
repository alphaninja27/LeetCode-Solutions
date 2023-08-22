class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        def dfs(r,c,root):
            character = board[r][c]
            #get to next node 
            cur = root[character]
            '''
            the reason why we use pop method is because
            we don't want to add the same word to result
            once we found it.
            Additionaly, we store value of "#" as word
            because, initially, we stored word itself as value of key.
            '''
            word = cur.pop("#",False)
            if word:
            #add to result if current node is end of word
                res.append(word)

            #mark current character as visited
            board[r][c] = "*"

            #for each direction apply dfs
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = r + dirx, c + diry
                if 0 <= curx < ROWS and 0 <= cury < COLS and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            #restore to its value once we done 
            board[r][c] = character

            '''
            because we popped "#" from cur if it is end of word
            we can check that it was been added and there is no need of it
            with this if condition. Hence, just delete node from root.
            '''
            if not cur:
                root.pop(character)
            
        #create trie
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            #store word itself for last node in each word
            cur["#"] = word

        #resulting list 
        res = []

        ROWS,COLS = len(board),len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie:
                    dfs(r,c,trie)
        return res
