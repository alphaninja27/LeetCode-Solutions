class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(openCount, closedCount, currParenthesis):
            if (openCount == closedCount == n): # reached a valid answer --> add to result
                result.append(currParenthesis)
            
            elif openCount >= closedCount and openCount <= n:
                # need to ensure that openCount does not exceed n, we can still proceed with adding "(" and ")" because
                # we would need to close the current "(" and the (n + 1)th "(" will be discarded in the else clause
                # we can also add open or closed parenthses when openCount >= closedCount when the number of open/closed parentheses is still smaller than n.
                
                # Here, we can add open or closed parenthesis
                
                backtrack(openCount + 1, closedCount, currParenthesis + "(")
                backtrack(openCount, closedCount + 1, currParenthesis + ")")
                
                
            else: # no. of closed parenthesis > no. of open parenthesis --> invalid --> discard
                return
        
        # this is the only case we can start with
        backtrack(1, 0, "(")
            
            
        return result
