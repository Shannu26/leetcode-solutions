######################################################

#   Solved on Friday, 27 - 08 - 2021.

######################################################


######################################################

#   Approach 1 : With Recursion

#   Runtime: 27ms   -   84.40%
#   Memory: 14.1MB  -   86.56%

######################################################

"""
    The Logic is similar in both cases of with and without recursion.
    In recursive approach the stack is automatically maintained by the complier.
    In non-recursive approach we manually declare the stack.

    Only the order in which strings are added to that stack are different.
    Refer to the picture attached
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "": return []
        
        keypad = { '2' : 'abc', '3' : 'def', 
                   '4' : 'ghi', '5' : 'jkl',
                   '6' : 'mno', '7' : 'pqrs', 
                   '8' : 'tuv', '9' : 'wxyz'
                 }
        
        result = []
        
        def process(string, index):
            if len(string) == len(digits):
                result.append(string)
                return
            for char in keypad[digits[index]]: process(string + char, index + 1)
        
        process("", 0)
        
        return result

######################################################

#   Approach 2 : Without Recursion

#   Runtime: 28ms   -   84.25%
#   Memory: 14.1MB  -   86.56%

######################################################

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "": return []
        
        keypad = { '2' : 'abc', '3' : 'def', 
                   '4' : 'ghi', '5' : 'jkl',
                   '6' : 'mno', '7' : 'pqrs', 
                   '8' : 'tuv', '9' : 'wxyz'
                 }
        
        stack = [""]
        for i in range(len(digits)):
            while len(stack[0]) == i:
                string = stack.pop(0)
                for char in keypad[digits[i]]:
                    stack.append(string + char)
        
        return stack