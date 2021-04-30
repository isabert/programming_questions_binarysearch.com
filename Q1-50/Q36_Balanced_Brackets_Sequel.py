class Solution:
    def solve(self, s):
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # if char is a closing bracket
            if char in mapping:
                # Pop the top most element else #, the top most element must be an opening bracket
                # of the same type
                top = stack.pop() if stack else "#"

                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        # if the stack is empty, we have a valid expression
        # the stack wont be empty for cases like (()
        return not stack



    def solve_alt(self, s):
        stack = []
        opening_set = ['(', '{', '[']
        closing_set = [')', '}', ']']

        for c in s:
            if c in opening_set:
                i = opening_set.index(c)
                stack.append(closing_set[i])
            else:
                if(len(stack)==0):
                    return False
                elif(stack[len(stack)-1]!=c):
                    return False
                else:
                    stack.pop(len(stack)-1)

        if(len(stack)!=0):
            return False

        return True

