class Solution:
    def reverseParentheses(self, s: str) -> str:
        # (ed(etco)el) -> (edocteel) -> leetcode
        # count parenthesis in one pass
        # loop for how many parenthesis u found
        # build new string by reversing innermost parenthesis
        # ex: parenthesis = 4, loop for 4 loop for n, if n = ( add 1 to it when n = 3 everthing after is flipped until )
        # instead of building new string just use a stack so it already reverses it

        stack = []
        temp = []
       
        for l in s:
            if l == ")":
                # do operation for reversing until hitting "("
                while stack[-1] != "(":
                    temp.append(stack.pop()) 
                stack.pop()
                stack.extend(temp)
                temp = []

            else:
                stack.append(l)

        return ''.join(map(str, stack))

        